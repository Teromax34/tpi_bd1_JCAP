
"""
TPI Base de Datos I - Etapa 5: Prototipo de pantallas (version consola)

IMPORTANTE: es solo un prototipo visual. No guarda datos, no tiene logica
de negocio y no se conecta a MySQL (tal como pide la consigna).
Los campos de cada pantalla salen de las tablas del modelo logico:
Localidad, Zona, Cliente, Telefono, Empleado, Producto, Pedido,
DetallePedido, Pago y SeguimientoPedido.
"""

ANCHO = 70


def linea(c="="):
    print(c * ANCHO)


def titulo(texto, finalidad):
    print()
    linea()
    print(texto.center(ANCHO))
    linea()
    print("Finalidad: " + finalidad)
    linea("-")


def campos(lista):
    """Muestra un formulario: cada campo con su casillero vacio."""
    for nombre in lista:
        print(f"  {nombre:<28}: [______________________]")


def tabla(cabeceras, filas, anchos):
    fmt = "  " + " | ".join(f"{{:<{a}}}" for a in anchos)
    print(fmt.format(*cabeceras))
    print("  " + "-+-".join("-" * a for a in anchos))
    for f in filas:
        print(fmt.format(*[str(x) for x in f]))


def pausa():
    input("\n  (Enter para volver al menu)")


# ---------------------------------------------------------------- pantallas
def pantalla_clientes():
    titulo("CLIENTES - Alta y consulta",
           "Cargar al cliente una sola vez y reutilizarlo en cada pedido.")
    print("  Datos del cliente (tabla Cliente / Zona / Localidad)")
    campos(["Nro. de cliente (auto)", "DNI", "Apellido", "Nombre", "Direccion",
            "Tipo de cliente (lista)", "Localidad (lista)",
            "Zona (lista segun localidad)"])
    print("\n  Telefonos (tabla Telefono, un cliente puede tener varios)")
    tabla(["Nro telefono", "Tipo"], [["353-4112233", "Celular"],
                                      ["353-4520000", "Fijo"]], [16, 12])
    print("\n  [Guardar]  [Cancelar]  [Buscar por DNI/Apellido]")
    pausa()


def pantalla_nuevo_pedido():
    titulo("NUEVO PEDIDO - reemplaza la ficha en papel",
           "Registrar el pedido (cabecera) y sus trabajos (detalle).")
    print("  CABECERA (tabla Pedido)")
    campos(["N de pedido (auto)", "Cliente (buscar)", "Fecha de ingreso",
            "Fecha de entrada", "Fecha de salida (prevista)", "Observaciones"])
    print("\n  DETALLE - trabajos del pedido (tabla DetallePedido)")
    campos(["Producto (lista)", "Material (lista)",
            "Ancho (cm)", "Largo (cm)", "Cantidad", "Acabado (margen/iman..)",
            "Indicaciones", "Precio unitario"])
    print("\n  Trabajos cargados:")
    tabla(["#", "Producto", "Material", "Medida", "Cant", "P.Unit"],
          [[1, "Impresion foto", "Papel Mate", "10x15", 10, "$ 300"],
           [2, "Gigantografia", "Lona Front", "200x100", 1, "$ 18000"]],
          [2, 15, 11, 9, 4, 8])
    print("\n  [Agregar trabajo]  [Quitar]  [Guardar pedido]  [Cancelar]")
    pausa()


def pantalla_consulta_pedidos():
    titulo("CONSULTA DE PEDIDOS",
           "Buscar pedidos y ver en que etapa estan (hoy se hace a mano).")
    print("  Filtros: Nro pedido [____]  Cliente [____]  Desde [____]  Hasta [____]\n")
    tabla(["Nro", "Cliente", "Ingreso", "Salida", "Estado", "Pagado"],
          [[43646, "Ivana", "26/08", "28/08", "Terminado", "SI"],
           [43647, "Perez, Juan", "26/08", "30/08", "En proceso", "NO"],
           [43648, "Gomez, Maria", "27/08", "-", "Pendiente", "Parcial"]],
          [6, 14, 8, 8, 11, 8])
    print("\n  [Ver detalle]  [Modificar]  [Imprimir comprobante]")
    pausa()


def pantalla_seguimiento():
    titulo("SEGUIMIENTO DEL PEDIDO - control interno",
           "Registrar quien hizo Descarga, Impresion, Facturacion y Despacho.")
    campos(["N de pedido", "Empleado (lista)", "Tipo de trabajo",
            "Fecha y hora (auto)"])
    print("      Tipo de trabajo: Descarga / Impresion / Facturacion / Despacho")
    print("\n  Historial del pedido 43646 (tabla SeguimientoPedido):")
    tabla(["Fecha y hora", "Empleado", "Trabajo"],
          [["26/08 09:10", "Lopez, Ana", "Descarga"],
           ["26/08 10:30", "Diaz, Pedro", "Impresion"],
           ["26/08 15:00", "Lopez, Ana", "Facturacion"],
           ["27/08 11:00", "Diaz, Pedro", "Despacho"]], [12, 14, 12])
    print("\n  [Registrar]  [Cancelar]")
    pausa()


def pantalla_pagos():
    titulo("PAGOS",
           "Registrar los pagos de un pedido (puede haber senias/varios pagos).")
    campos(["N de pedido", "Fecha de pago", "Medio de pago", "Monto"])
    print("\n  Pagos del pedido 43646 (tabla Pago):")
    tabla(["Fecha", "Medio", "Monto"],
          [["26/08", "Efectivo", "$ 1000"], ["28/08", "Transferencia", "$ 2000"]],
          [10, 15, 10])
    print("\n  Total pedido: $ 3000   Pagado: $ 3000   Saldo: $ 0")
    print("\n  [Registrar pago]  [Cancelar]")
    pausa()


def pantalla_productos():
    titulo("PRODUCTOS / CATALOGO",
           "Mantener lo que se vende y su precio base (alta, baja, cambios).")
    campos(["Nombre", "Categoria (lista)",
            "Precio base"])
    print()
    tabla(["Id", "Nombre", "Categoria", "Precio base"],
          [[1, "Impresion foto", "Impresion", "$ 250"],
           [2, "Ampliacion 30x45", "Ampliacion", "$ 2500"],
           [3, "Gigantografia", "Gigantografia", "$ 9000"]], [3, 18, 14, 11])
    print("\n  [Nuevo]  [Modificar]  [Eliminar]")
    pausa()


def pantalla_empleados():
    titulo("EMPLEADOS",
           "Administrar el personal que interviene en los pedidos.")
    campos(["DNI", "Apellido", "Nombre", "Telefono", "Rol"])
    print()
    tabla(["Id", "Apellido y nombre", "Rol"],
          [[1, "Lopez, Ana", "Administracion"],
           [2, "Diaz, Pedro", "Impresor"]], [3, 20, 16])
    print("\n  [Nuevo]  [Modificar]  [Eliminar]")
    pausa()


# --------------------------------------------------------------------- menu
OPCIONES = {
    "1": ("Nuevo pedido", pantalla_nuevo_pedido),
    "2": ("Consulta de pedidos", pantalla_consulta_pedidos),
    "3": ("Seguimiento del pedido (control interno)", pantalla_seguimiento),
    "4": ("Pagos", pantalla_pagos),
    "5": ("Clientes", pantalla_clientes),
    "6": ("Productos / catalogo", pantalla_productos),
    "7": ("Empleados", pantalla_empleados),
}


def main():
    while True:
        print()
        linea()
        print("SISTEMA DE GESTION DE IMPRESIONES - PROTOTIPO".center(ANCHO))
        linea()
        for k, (nombre, _) in OPCIONES.items():
            print(f"  {k}. {nombre}")
        print("  0. Salir")
        op = input("\n  Elija una opcion: ").strip()
        if op == "0":
            print("  Fin del prototipo.")
            break
        if op in OPCIONES:
            OPCIONES[op][1]()
        else:
            print("  Opcion invalida.")


if __name__ == "__main__":
    main()
