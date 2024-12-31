import statistics
from datetime import datetime

class Experimento:
    def __init__(self, nombre, fecha_realizacion, tipo_experimento, resultados):
        self.nombre = nombre
        self.fecha_realizacion = fecha_realizacion
        self.tipo_experimento = tipo_experimento
        self.resultados = resultados
    
    def __str__(self):
        return (f"Nombre del Experimento: {self.nombre}\n"
                f"Fecha de Realización: {self.fecha_realizacion}\n"
                f"Tipo de Experimento: {self.tipo_experimento}\n"
                f"Resultados: {self.resultados}")

    def promedio_resultados(self):
        return sum(self.resultados) / len(self.resultados) if self.resultados else 0
    
    def maximo_resultados(self):
        return max(self.resultados) if self.resultados else None
    
    def minimo_resultados(self):
        return min(self.resultados) if self.resultados else None

def validar_resultados(resultado_str):
    try:
        resultados = [float(x) for x in resultado_str.split(",")]
        return resultados
    except ValueError:
        print("Error: Por favor ingresa solo números válidos separados por comas.")
        return []

def validar_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        return fecha
    except ValueError:
        print("Error: La fecha no tiene el formato correcto. Usa el formato YYYY-MM-DD.")
        return None

def agregar_experimento(experimentos):
    nombre = input("Ingresa el nombre del experimento: ")
    fecha_realizacion = input("Ingresa la fecha de realización (YYYY-MM-DD): ")
    fecha = validar_fecha(fecha_realizacion)
    if not fecha:
        return

    tipo_experimento = input("Ingresa el tipo de experimento: ")
    resultados_str = input("Ingresa los resultados separados por comas: ")
    resultados = validar_resultados(resultados_str)
    if resultados:
        experimento = Experimento(nombre, fecha_realizacion, tipo_experimento, resultados)
        experimentos.append(experimento)
        print(f"Experimento '{nombre}' agregado con éxito.")
    else:
        print("El experimento no pudo ser agregado debido a resultados inválidos.")

def mostrar_experimentos(experimentos):
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    for experimento in experimentos:
        print(experimento)
        print(f"Promedio: {experimento.promedio_resultados()}")
        print(f"Máximo: {experimento.maximo_resultados()}")
        print(f"Mínimo: {experimento.minimo_resultados()}")
        print("----------------------------")

def analizar_experimentos(experimentos):
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    for experimento in experimentos:
        promedio = experimento.promedio_resultados()
        maximo = experimento.maximo_resultados()
        minimo = experimento.minimo_resultados()
        print(f"\nAnálisis de {experimento.nombre}")
        print(f"Promedio de resultados: {promedio}")
        print(f"Máximo de resultados: {maximo}")
        print(f"Mínimo de resultados: {minimo}")

def comparar_experimentos(experimentos):
    if not experimentos:
        print("No hay experimentos registrados.")
        return

    for i, experimento in enumerate(experimentos):
        promedio = experimento.promedio_resultados()
        print(f"Promedio de resultados del experimento {i+1} ({experimento.nombre}): {promedio}")
    
    if len(experimentos) >= 2:
        prom_exp1 = experimentos[0].promedio_resultados()
        prom_exp2 = experimentos[1].promedio_resultados()
        if prom_exp1 > prom_exp2:
            print(f"{experimentos[0].nombre} tiene un mayor promedio de resultados que {experimentos[1].nombre}.")
        elif prom_exp1 < prom_exp2:
            print(f"{experimentos[1].nombre} tiene un mayor promedio de resultados que {experimentos[0].nombre}.")
        else:
            print(f"Ambos experimentos tienen el mismo promedio de resultados.")
    else:
        print("No hay suficientes experimentos para comparar.")

def generar_informe(experimentos):
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    try:
        with open("Informe_Experimentos.txt", "w") as archivo:
            for experimento in experimentos:
                archivo.write(f"Nombre: {experimento.nombre}\n")
                archivo.write(f"Fecha del experimento: {experimento.fecha_realizacion}\n")
                archivo.write(f"Categoría: {experimento.tipo_experimento}\n")
                archivo.write(f"Resultados: {', '.join(map(str, experimento.resultados))}\n")
                archivo.write(f"Promedio de Resultados: {experimento.promedio_resultados()}\n")
                archivo.write(f"Máximo: {experimento.maximo_resultados()}\n")
                archivo.write(f"Mínimo: {experimento.minimo_resultados()}\n")
                archivo.write("\n")
        print("Informe generado con éxito.")
    except Exception as e:
        print(f"Error al generar el informe: {e}")

def borrar_experimento(experimentos):
    if not experimentos:
        print("No hay experimentos registrados.")
        return

    nombre = input("Ingresa el nombre del experimento que deseas eliminar: ")
    encontrado = False

    for experimento in experimentos:
        if experimento.nombre.lower() == nombre.lower():
            experimentos.remove(experimento)
            print(f"El experimento '{nombre}' ha sido eliminado con éxito.")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró un experimento con el nombre '{nombre}'.")

def mostrar_menu():
    print("------------DAT0S DE ACCESO----------------------")
    print("\nMenú del Programa: ")
    print("1. Agregar un nuevo experimento")
    print("2. Ver todos los experimentos")
    print("-----------MANEJO DE DATOS------------------------")
    print("3. Análisis de resultados")
    print("4. Comparar los experimentos")
    print("5. Generar Informes de experimentos")
    print("6. Borrar un experimento")
    print("7. Salir del programa")
    opcion = input("Elige una opción: ")
    return opcion

def main():
    experimentos = []
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            agregar_experimento(experimentos)
        elif opcion == "2":
            mostrar_experimentos(experimentos)
        elif opcion == "3":
            analizar_experimentos(experimentos)
        elif opcion == "4":
            comparar_experimentos(experimentos)
        elif opcion == "5":
            generar_informe(experimentos)
        elif opcion == "6":
            borrar_experimento(experimentos)
        elif opcion == "7":
            print("¡Gracias por usar el programa! ¡Hasta luego!")
            break  # Salir del ciclo y terminar el programa
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
