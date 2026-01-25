/** @odoo-module **/

import { Component, useState, onWillStart } from '@odoo/owl';
import { registry } from '@web/core/registry';
import { _t } from "@web/core/l10n/translation";


export class OwlProductsRMA extends Component {
    static template = 'owl_website_rma.OwlProductsRMA';

    setup() {
        this.state = useState({
            products: [],
            filteredProducts: [],
            operations: [],
            searchTerm: '',
            selectedProductId: null,
            selectedProductName: '',
            selectedProductCategory: '',
            selectedOperationId: null,
            description: '',
            showModal: false,  
            errorMessage: '',  
            loading: false,  
            offset: 0,  
            limit: 20,  
        });

        // Métodos vinculados
        this.onSearchChange = this.onSearchChange.bind(this);
        this.onProductSelect = this.onProductSelect.bind(this);
        this.onOperationChange = this.onOperationChange.bind(this);
        this.onDescriptionChange = this.onDescriptionChange.bind(this);
        this.submitForm = this.submitForm.bind(this);
        this.closeModal = this.closeModal.bind(this);
        this.onScroll = this.onScroll.bind(this);

        onWillStart(async () => {
            console.log("Iniciando carga de datos...");
            await this.getOperations();
            await this.getProducts('');
            this.state.loading = false;
        });

        window.addEventListener("scroll", this.onScroll);
    }

    // OBTENER PRODUCTOS CON FILTRO CORREGIDO Y MANEJO DE ERRORES
    async getProducts(filterTerm, offset = 0, limit = this.state.limit) {
        console.log("🔍 Buscando productos con filtro:", filterTerm, "offset:", offset);

        try {
            this.state.loading = true;

            // Evita que el filtro se pase vacío
            const domain = filterTerm
                ? ['|', ['name', 'ilike', filterTerm], ['default_code', 'ilike', filterTerm]]
                : [];

            const products = await this.env.services.orm.searchRead(
                'product.product',
                domain,
                ['name', 'default_code', 'categ_id','category_breadcrumb', 'image_1920'],
                { limit: limit, offset: offset, context: { "active_test": false } }
            );

            if (!products || products.length === 0) {
                console.warn("⚠ No se encontraron productos en la base de datos.");
            } else {
                console.log("Productos obtenidos:", products);
            }

            if (offset === 0) {
                this.state.products = products;
            } else {
                this.state.products = [...this.state.products, ...products];
            }

            this.state.filteredProducts = this.state.products;
            this.state.offset += limit;
            this.state.loading = false;
        } catch (error) {
            console.error("Error al obtener productos:", error);

            // Capturar detalles del error RPC de Odoo
            if (error.message.includes("Odoo Server Error")) {
                alert("Error en el servidor de Odoo. Revisa los logs para más detalles.");
            } else {
                alert("Error inesperado al obtener productos.");
            }

            this.state.loading = false;
        }
    }

    // OBTENER OPERACIONES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    async getOperations() {
        try {
            console.log("Cargando operaciones...");
            const operations = await this.env.services.orm.searchRead(
                'rma.operation', [], ['id', 'name'],
                { context: { lang: "de_DE" } }
            );
            this.state.operations = operations;
            console.log("Operaciones cargadas:", operations.length);
        } catch (error) {
            console.error("Error al obtener operaciones:", error);
        }
    }

    // BUSCAR PRODUCTOS SEGÚN INPUT DEL USUARIO
    onSearchChange(ev) {
        const searchTerm = ev.target.value.toLowerCase();
        console.log("🔍 Usuario buscando:", searchTerm);

        if (searchTerm.length >= 3) {
            this.state.searchTerm = searchTerm;
            this.state.offset = 0;
            this.getProducts(searchTerm);
        }
    }

    // SELECCIONAR PRODUCTO
    onProductSelect(product) {
        console.log("Producto seleccionado:", product.name);
        this.state.selectedProductId = product.id;
        this.state.selectedProductName = product.name;
        this.state.selectedProductCategory = product.categ_id ? product.categ_id[1] : 'Sin categoría';
        this.state.searchTerm = product.name;
        this.state.filteredProducts = [];


        // Guardar trail de categoría para miga de pan
        if (product.category_trail) {
            this.state.categoryTrail = product.category_trail;
        } else {
            this.state.categoryTrail = [product.categ_id]; // fallback si no hay trail
        }
    }

    // SELECCIONAR OPERACIÓN
    onOperationChange(ev) {
        this.state.selectedOperationId = ev.target.value;
    }

    // CAMBIAR DESCRIPCIÓN
    onDescriptionChange(ev) {
        this.state.description = ev.target.value;
    }

    // CERRAR MODAL DE ERROR
    closeModal() {
        this.state.showModal = false;
    }

    // ENVÍO DE FORMULARIO CON VALIDACIONES
    async submitForm(ev) {
        ev.preventDefault();

        if (!this.state.selectedProductId || !this.state.selectedOperationId || !this.state.description) {
            console.warn("⚠ Falta completar el formulario.");
            this.state.errorMessage = 'Producto, operación y descripción son obligatorios.';
            this.state.showModal = true;
            return;
        }

        const formData = new FormData();
        formData.append('product_id', this.state.selectedProductId);
        formData.append('operation_id', this.state.selectedOperationId);
        formData.append('description', this.state.description);

        try {
            console.log("📤 Enviando formulario...");
            const response = await fetch('/custom_website_rma', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                console.log("Formulario enviado con éxito.");
                window.location.href = "/rma_thanks_page";
            } else {
                console.error("Error al enviar formulario.");
                this.state.errorMessage = 'Error al enviar el formulario. Intente nuevamente.';
                this.state.showModal = true;
            }
        } catch (error) {
            console.error("Error de red al enviar el formulario:", error);
            this.state.errorMessage = 'Error de red al enviar el formulario.';
            this.state.showModal = true;
        }
    }

    // CARGA MÁS PRODUCTOS CON SCROLL INFINITO
    onScroll() {
        const nearBottom = window.innerHeight + window.scrollY >= document.body.offsetHeight - 100;
        if (nearBottom && !this.state.loading) {
            console.log("Cargando más productos...");
            this.getProducts(this.state.searchTerm, this.state.offset);
        }
    }
}

registry.category('public_components').add('owl_website_rma.OwlProductsRMA', OwlProductsRMA);
