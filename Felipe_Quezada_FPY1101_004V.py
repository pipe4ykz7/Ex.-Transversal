import random
import csv
import math

trabajadores = [
    {"nombre": "Juan Pérez"},
    {"nombre": "María García"},
    {"nombre": "Carlos López"},
    {"nombre": "Ana Martínez"},
    {"nombre": "Pedro Rodríguez"},
    {"nombre": "Laura Hernández"},
    {"nombre": "Miguel Sánchez"},
    {"nombre": "Isabel Gómez"},
    {"nombre": "Francisco Díaz"},
    {"nombre": "Elena Fernández"}
]

sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    print("Clasificación de Sueldos:")
    categorias = {
        "Sueldos menores a $800,000": [],
        "Sueldos entre $800,000 y $2,000,000": [],
        "Sueldos superiores a $2,000,000": []
    }

    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            categorias["Sueldos menores a $800,000"].append((trabajador["nombre"], sueldo))
        elif 800000 <= sueldo <= 2000000:
            categorias["Sueldos entre $800,000 y $2,000,000"].append((trabajador["nombre"], sueldo))
        else:
            categorias["Sueldos superiores a $2,000,000"].append((trabajador["nombre"], sueldo))
    
    for categoria, empleados in categorias.items():
        print(f"{categoria} - Total: {len(empleados)}")
        for empleado in empleados:
            print(f"Nombre: {empleado[0]}, Sueldo: ${empleado[1]}")

def ver_estadisticas():
    if not sueldos:
        print("Aún no se han asignado los sueldos.")
        return
    
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))

    print(f"Estadísticas de Sueldos:")
    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${sueldo_promedio:.2f}")
    print(f"Media geométrica de sueldos: ${sueldo_geom:.2f}")

def reporte_sueldos():
    if not sueldos:
        print("Aún no se han asignado los sueldos.")
        return
    
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador["nombre"], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"Nombre empleado: {trabajador['nombre']}, Sueldo Base: ${sueldo}, Descuento Salud: ${descuento_salud:.2f}, Descuento AFP: ${descuento_afp:.2f}, Sueldo Líquido: ${sueldo_liquido:.2f}")

def salir_programa():
    print("Finalizando programa…")
    print("Desarrollado por Felipe Quezada")
    print("RUT 21751881-4")

def menu():
    while True:
        print("\nMenu Gestion Sueldos")
        print("[1] - Asignar sueldos aleatorios")
        print("[2] - Clasificar sueldos")
        print("[3] - Ver estadísticas")
        print("[4] - Generar reporte de sueldos")
        print("[5] - Salir del programa")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                asignar_sueldos_aleatorios()
            elif opcion == 2:
                clasificar_sueldos()
            elif opcion == 3:
                ver_estadisticas()
            elif opcion == 4:
                reporte_sueldos()
            elif opcion == 5:
                salir_programa()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    menu()