import keyword

import numpy as np
import streamlit as st
import pandas as pd
from six import with_metaclass
from streamlit.runtime.state import session_state

import librería_clases_proyecto1 as lc
import libreria_funciones_proyecto1 as lf

# Configuracion de la pagina:
st.set_page_config(
    page_title="Proyecto Python Fundamentals",
    page_icon="🐍",
    layout="wide"
)

# Estilos visuales suaves compatibles con modo claro y oscuro
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2.5rem;
            max-width: 1200px;
        }

        h1, h2, h3 {
            color: var(--text-color);
        }

        section[data-testid="stSidebar"] {
            background-color: var(--secondary-background-color);
            border-right: 1px solid rgba(128, 128, 128, 0.22);
        }

        section[data-testid="stSidebar"] * {
            color: var(--text-color);
        }

        .stButton > button {
            border-radius: 8px;
            font-weight: 600;
            padding: 0.45rem 1rem;
        }

        div[data-testid="stMetric"] {
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.24);
            border-radius: 10px;
            padding: 0.8rem 1rem;
        }

        div[data-testid="stMetric"] * {
            color: var(--text-color);
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid rgba(128, 128, 128, 0.24);
            border-radius: 10px;
            overflow: hidden;
        }

        div[data-testid="stAlert"] {
            border-radius: 8px;
        }

        hr {
            border: none;
            border-top: 1px solid rgba(128, 128, 128, 0.25);
            margin: 1.25rem 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

##### Home ######
# Titulo principal:
st.title("🐍 Proyecto Python Fundamentals")

# Agregando memoria a streamlit con "st.session_state"
# ¿Ya existe una lista llamada "movimientos" dentro de la memoria de la aplicación?
# Si la respuesta es NO:
# ejecuta la siguiente línea.

if "movimientos" not in st.session_state:
    st.session_state["movimientos"] = []

# Menu lateral:
st.sidebar.title("Menú principal")
st.sidebar.caption("Proyecto académico con Streamlit")

opcion = st.sidebar.selectbox(
    "Seleccione una sección:",
    ["Home",
     "Ejercicio 1",
     "Ejercicio 2",
     "Ejercicio 3",
     "Ejercicio 4", ]
)

###### Ejercicio 1 #########
# Navegacion:
if opcion == "Home":
    st.header("Inicio")

    st.subheader("Proyecto desarrollado en Streamlit")

    st.markdown("""
    Este proyecto integra conceptos fundamentales de programación en Python
    mediante una interfaz interactiva construida con Streamlit.

    La aplicación contiene ejercicios relacionados con listas, arreglos con NumPy,
    funciones externas, clases y programación orientada a objetos.
    """)

    st.markdown("---")

    # Logos centrados y con tamaños equilibrados
    col_espacio1, col_python, col_dmc, col_espacio2 = st.columns([1, 1.2, 1.2, 1])

    with col_python:
        st.image(
            "Python_logo.png",
            width=150
        )
        st.caption("Python")

    with col_dmc:
        st.image(
            "DMC.png",
            width=150
        )
        st.caption("DMC Institute")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Información del estudiante")
        st.write("**Nombre:** Cesar Ospiño Salas")
        st.write("**Especialización:** Python for Analytics")
        st.write("**Año:** 2026")

    with col2:
        st.subheader("Tecnologías utilizadas")
        st.write("• Python")
        st.write("• Streamlit")
        st.write("• NumPy")
        st.write("• Pandas")

##### Ejercicio 1 #####
elif opcion == "Ejercicio 1":
    st.header("Ejercicio 1 - Flujo de caja")

    st.markdown("""
    En este ejercicio se registran movimientos de ingreso y gasto.

    La aplicación almacena cada movimiento, muestra los registros
    en una tabla y calcula el total de ingresos, el total de gastos
    y el saldo disponible.
    """)

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        concepto = st.text_input("Concepto")

    with col2:
        tipo = st.selectbox(
            "Tipo de movimiento",
            ["Ingreso", "Gasto"]
        )

    with col3:
        valor = st.number_input(
            "Valor del movimiento",
            min_value=0.0,
            step=1.0,
        )

    # Creacion de boton:
    agregar = st.button("Agregar movimiento")
    # Si el boton "agregar movimiento" fue presionado, se ejecuta el codigo que esta dentro del if
    # strip(), elimina los espacios al inicio y al final
    # st.error(), detecta que la caja de texto esta vacia y lanza un error.
    # else , si todo esta correcto, agrega un valor
    if agregar:
        if concepto.strip() == "":
            st.error("Debe ingresar un concepto")
        else:
            st.session_state["movimientos"].append(
                [concepto, tipo, valor]
            )
            st.success("Movimiento agregado")

    st.markdown("---")
    st.subheader("Movimientos registrados")

    # Creacion de tabla:
    df = pd.DataFrame(
        st.session_state.movimientos,
        columns=["concepto", "tipo", "valor"]
    )

    # "st.dataframe" -> muestra una tabla interactiva
    # "use_container_width" -> Hace que la tabla aproveche el ancho disponible de la página.
    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # Variables acumuladoras:
    # Al principio valen 0 porque no se ha recorrido la lista
    total_ingresos = 0
    total_gastos = 0

    # Agregamos el bucle for y por cada vuelta, va acumulando(+=) valores en las variables
    # total_ingresos y total_gastos
    for movimiento in st.session_state.movimientos:
        if movimiento[1] == "Ingreso":
            total_ingresos += movimiento[2]
        else:
            total_gastos += movimiento[2]

    # Calcula el dinero restante
    saldo = total_ingresos - total_gastos

    # "st.columns", crea 3 columnas del mismo tamaño
    # “with col1:”, quiere decir que todo lo que se escriba ahi, se colocara en la columna 1
    # st.metric(), Es un componente pensado para mostrar indicadores o KPI (Key Performance Indicators)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total ingresos", total_ingresos)

    with col2:
        st.metric("Total gastos", total_gastos)

    with col3:
        st.metric("Saldo", saldo)

    if saldo > 0:
        st.success("El flujo de caja esta a favor.")
    elif saldo < 0:
        st.error("El flujo de caja esta en contra.")
    else:
        st.info("El flujo de caja esta equilibrado.")

#### Ejercicio 2 ####
elif opcion == "Ejercicio 2":
    st.header("Ejercicio 2 - Registro de productos")

    # Pregunta si todavía no existe una variable llamada productos dentro de la memoria de Streamlit.
    # Crea una lista vacía donde posteriormente guardaremos los productos registrados.
    if "productos" not in st.session_state:
        st.session_state.productos = []

    st.markdown("""
    En este ejercicio se registran productos mediante un formulario.

    Los datos ingresados se almacenan, se procesan utilizando NumPy
    y posteriormente se muestran en una tabla construida con Pandas.
    """)

    # Guarda el texto escrito por el usuario
    col1, col2 = st.columns(2)

    with col1:
        nombre_producto = st.text_input(
            "Nombre del producto",
        )

    # Guarda la opcion seleccionada por el usuario
    with col2:
        categoria = st.selectbox(
            "Categoria",
            [
                "Tecnologia",
                "Hogar",
                "Alimentos",
                "Ropa",
                "Otros"
            ]
        )

    col3, col4 = st.columns(2)

    # Guarda el precio unitario del producto
    with col3:
        precio = st.number_input(
            "Precio del producto",
            min_value=0.01,
            step=1.0,
        )

    # Guarda la cantidad de unidades vendidas
    # Usamos valores como enteros
    with col4:
        cantidad = st.number_input(
            "Cantidad vendida",
            min_value=1,
            step=1
        )

    # Calcula el total de la venta
    total = precio * cantidad

    # Crea el boton
    agregar_producto = st.button(
        "Agregar producto")

    # Se ejecuta cuando el usuario presiona el botón
    if agregar_producto:
        if nombre_producto.strip() == "":
            st.error("Debe ingresar el nombre del producto")
        else:
            st.session_state.productos.append(
                [
                    nombre_producto,
                    categoria,
                    precio,
                    cantidad,
                    total
                ]
            )
            st.success("Producto agregado correctamente")

    st.markdown("---")
    st.subheader("Productos registrados")

    # Creando dataframe con "pandas":
    df_productos = pd.DataFrame(
        st.session_state.productos,
        columns=[
            "Producto",
            "Categoria",
            "Precio",
            "Cantidad",
            "Total"
        ]
    )

    # Utiliza todo el ancho de la pantalla
    st.dataframe(df_productos, use_container_width=True)

    # # Convierte los precios registrados en un arreglo de NumPy = np.array()
    # len(), muestra la cantidad de valores que hay en session_state
    if len(st.session_state.productos) > 0:
        precios = np.array(
            [  # Esto se llama comprensión de listas (list comprehension).
                producto[2]
                for producto in st.session_state.productos
            ]
        )

        # mean(), Calcula estadísticas utilizando NumPy:
        precio_promedio = np.mean(precios)
        precio_maximo = np.max(precios)
        precio_minimo = np.min(precios)

        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                "Precio Promedio",
                f"S/. {precio_promedio:.2f}"
            )
        with col2:
            st.metric(
                "Precio Maximo",
                f"S/. {precio_maximo:.2f}"
            )
        with col3:
            st.metric(
                "Precio Minimo",
                f"S/. {precio_minimo:.2f}"
            )


###### Ejercicio 3 ######
elif opcion == "Ejercicio 3":
    st.header("Ejercicio 3 - Función externa")

    # Pregunta si aun no existe una variable llamada: "historial_prestamos"
    # Si no existe, crea una vacia
    if "historial_prestamos" not in st.session_state:
        st.session_state.historial_prestamos = []

    funcion_seleccionada = st.selectbox(
        "Seleccione una funcion",
        ["Calcular cuota de prestamo frances"]
    )

    # "monto", variable donde se almacenara lo ingresado por el usuario
    # "st.number_input", sirve para que el usuario escriba un numero
    # "Monto del prestamo", etiqueta que vera el usuario.
    # "min_value=1000.0", le indicamos a streamlit no permitir montos menores a 1000.0
    # "step=100.0", Cada clic en las flechas aumentará o disminuirá el valor de 100 en 100
    col1, col2, col3 = st.columns(3)

    with col1:
        monto = st.number_input(
            "Monto del prestamo",
            min_value=1000.0,
            step=100.0,
        )

    # "tasa", Guardará el porcentaje de interés anual.
    # "min_value=0.1", no permitira tasas negativas ni una tasa de 0%
    # "step=0.1", cada clic aumentara 0.1. Ejemplo: 5.0, 5.1, 5.2 ...
    with col2:
        tasa = st.number_input(
            "Tasa anual (%)",
            min_value=0.1,
            step=0.1,
        )

    # "plazo", Será la variable donde guardaremos la cantidad de meses del préstamo.
    # "min_value", plazo minimo de meses debe ser 1
    # "step = 1", cada clic aumentara un mes
    with col3:
        plazo = st.number_input(
            "Plazo (meses)",
            min_value=1,
            step=1,
        )

    # Agregamos boton calcular:
    calcular = st.button("Calcular prestamo")

    # "lf.calcular_cuota_prestamo_frances" devuelve un diccionario:
    # "resultado" sera la variable que contiene el diccionario
    if calcular:
        resultado = lf.calcular_cuota_prestamo_frances(
            monto,
            tasa,
            plazo
        )

        cuota = resultado["cuota_mensual"]
        total_pagado = resultado["total_pagado"]
        interes_total = resultado["interes_total"]

        # Guarda cada simulacion realizada por el usuario
        st.session_state.historial_prestamos.append(
            [
                monto,
                tasa,
                plazo,
                cuota,
                total_pagado,
                interes_total
            ]
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Cuota mensual", f"S/ {cuota:.2f}")
        with col2:
            st.metric("Total pagado", f"S/ {total_pagado:.2f}")
        with col3:
            st.metric("Interes total", f"S/ {interes_total:.2f}")

    if len(st.session_state.historial_prestamos) > 0:
        df_historial = pd.DataFrame(
            st.session_state.historial_prestamos,
            columns=[
                "Monto",
                "Tasa anual",
                "Plazo en meses",
                "Cuota mensual",
                "Total pagado",
                "Interes total"
            ]
        )

        st.subheader("Historial de préstamos")
        st.dataframe(df_historial,
                     use_container_width=True)



###### Ejercicio 4 ######
elif opcion == "Ejercicio 4":
    st.header("Ejercicio 4 - CRUD de clases")

    # Si todavia no existe una variable llamada "empleados"dentro de sesion_state, la crea:
    if "empleados" not in st.session_state:
        st.session_state.empleados = []

    operacion_crud = st.selectbox(
        "Seleccione una operación",
        ["Crear", "Leer", "Actualizar", "Eliminar"]
    )

    # Crear #
    if operacion_crud == "Crear":
        nombre_empleado = st.text_input(
            "Nombre del empleado"
        )

        # El salario debe ser mayor a 0
        salario_base = st.number_input(
            "Salario base",
            min_value=0.01,
            step=100.0
        )

        # El bono debe estar entre 0 y 100
        porcentaje_bono = st.number_input(
            "Porcentaje bono",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

        # El descuento debe estar entre 0 y 100
        porcentaje_descuento = st.number_input(
            "Porcentaje de descuento",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

        # "Empleado" es la clase que se encuentra dentro del archivo
        crear_empleado = st.button(
            "Crear empleado"
        )

        if crear_empleado:
            if nombre_empleado.strip() == "":
                st.error("Debe ingresar el nombre del empleado")
            else:
                empleado = lc.Empleado(
                    nombre=nombre_empleado,
                    salario_base=salario_base,
                    porcentaje_bono=porcentaje_bono,
                    porcentaje_descuento=porcentaje_descuento
                )

                # Guarda el objeto creado. "append" lo agrega al final de la lista
                st.session_state.empleados.append(empleado)
                st.success("Empleado creado correctamente")

    # Leer #
    elif operacion_crud == "Leer":
        # Solo muestra la tabla si existen empleados registrados
        if len(st.session_state.empleados) == 0:
            st.warning("No existen empleados registrados")

        else:
            lista_resumenes = []

            for empleado in st.session_state.empleados:
                lista_resumenes.append(
                    empleado.resumen()
                )
            df_empleados = pd.DataFrame(
                lista_resumenes
            )

            st.subheader("Lista de empleados")

            st.dataframe(
                df_empleados,
                use_container_width=True
            )

    elif operacion_crud == "Actualizar":
        if len(st.session_state.empleados) == 0:
            st.warning("No existen empleados para actualizar")
        else:
            # Recorre toda la lista y extrae unicamente el nombre
            nombres_empleados = [
                empleado.nombre
                for empleado in st.session_state.empleados
            ]

            # El select muestra los nombres
            empleado_seleccionado = st.selectbox(
                "Seleccione el empleado",
                nombres_empleados,
                key="select_actualizar"
            )

            empleado_encontrado = None

            for empleado in st.session_state.empleados:
                # Compara el nombre del objeto por el seleccionado por el usuario:
                if empleado.nombre == empleado_seleccionado:
                    empleado_encontrado = empleado
                    break

            if empleado_encontrado is not None:
                nuevo_nombre = st.text_input(
                    "Nombre",
                    value=empleado_encontrado.nombre,
                    key=f"actualizar_nombre_{empleado_seleccionado}"
                )

                nuevo_salario = st.number_input(
                    "Salario base",
                    min_value=0.01,
                    value=float(empleado_encontrado.salario_base),
                    step=100.0,
                    key=f"actualizar_salario_{empleado_seleccionado}"
                )

                nuevo_bono = st.number_input(
                    "Porcentaje bono",
                    min_value=0.0,
                    max_value=100.0,
                    value=float(empleado_encontrado.porcentaje_bono),
                    step=1.0,
                    key=f"actualizar_bono_{empleado_seleccionado}"
                )

                nuevo_descuento = st.number_input(
                    "Porcentaje de descuento",
                    min_value=0.0,
                    max_value=100.0,
                    value=float(empleado_encontrado.porcentaje_descuento),
                    step=1.0,
                    key=f"actualizar_descuento_{empleado_seleccionado}"
                )
            actualizar_empleado = st.button(
                "Actualizar empleado")

            # Compureba si el usuario hizo clic en el boton
            if actualizar_empleado:

                # Evita que la caja no se quede en blanco
                if nuevo_nombre.strip() == "":
                    st.error("Debe ingresar el nombre del empleado")
                # Reemplaza los valores antiguos:
                else:
                    empleado_encontrado.nombre = nuevo_nombre
                    empleado_encontrado.salario_base = (nuevo_salario)
                    empleado_encontrado.porcentaje_bono = (nuevo_bono)
                    empleado_encontrado.porcentaje_descuento = (nuevo_descuento)

                    st.success("Empleado actualizado correctamente")

                    # st.rerun()

    # Eliminar #
    elif operacion_crud == "Eliminar":
        if len(st.session_state.empleados) == 0:
            st.warning("No existen empleados para eliminar")

        else:
            nombres_empleados = [
                empleado.nombre
                for empleado in st.session_state.empleados
            ]

            empleado_seleccionado = st.selectbox(
                "Seleccione un empleado",
                nombres_empleados,
                key="select_eliminar"
            )

            eliminar_empleado = st.button("Eliminar empleado")

            if eliminar_empleado:
                for empleado in st.session_state.empleados:
                    if empleado.nombre == empleado_seleccionado:
                        st.session_state.empleados.remove(empleado)
                        break

                st.success("Empleado eliminado correctamente")
                # st.rerun()
