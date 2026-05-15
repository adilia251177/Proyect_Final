"""

Archivo    : main.py  —  Programa principal
Descripción: Punto de entrada del sistema. Instancia los objetos,
             registra materias, notas y genera el reporte final.
=============================================================

CLASES UTILIZADAS:
    - Estudiante : modela al estudiante universitario
    - Materia    : modela cada asignatura cursada
    - Nota       : modela cada calificación obtenida

CONCEPTOS POO APLICADOS DEL MODULO PROGRAMACION1
    - Constructor (__init__) en las 3 clases
    - Instancia de objetos (Estudiante, Materia, Nota)
    - Creación y uso de métodos (matricular, agregar_nota,
      calcular_promedio, generar_reporte, etc.)
    - Composición: Estudiante contiene Materias;
                   Materia contiene Notas
=============================================================
"""

from estudiante import Estudiante
from materia   import Materia
from nota      import Nota


def main():
    """
    Función principal que ejecuta el Sistema de Gestión Académica.

    Demuestra:
      1. Instanciación de objetos con el constructor __init__
      2. Uso de métodos para registrar datos
      3. Generación de reporte académico final
    """

    print("\n" + "=" * 55)
    print("   SISTEMA DE GESTIÓN ACADÉMICA ESTUDIANTIL")
    print("   Universidad de Manizales — Programación I")
    print("=" * 55 + "\n")

    # ─────────────────────────────────────────────────────────
    # PASO 1: Instanciar el objeto Estudiante
    #         El constructor recibe todos los datos personales.
    # ─────────────────────────────────────────────────────────
    estudiante1 = Estudiante(
        codigo   = "2024-0158",
        nombre   = "Luz  Adilia Giraldo Vargas",
        carrera  = "Ingeniería Analitica Datos ",
        semestre = 3,
        email    = "lv.rios@umanizales.edu.co"
    )

    estudiante1.mostrar_perfil()

    # ─────────────────────────────────────────────────────────
    # PASO 2: Instanciar objetos Materia
    #         Cada materia tiene código, nombre, créditos,
    #         docente y horario.
    # ─────────────────────────────────────────────────────────
    print("\n--- Matriculando materias ---\n")

    prog1 = Materia(
        codigo   = "INF201",
        nombre   = "Programación I",
        creditos = 4,
        docente  = "Carlos Betancourt Correa",
        horario  = "Martes y Jueves  8:00 AM - 10:00 AM"
    )

    calculo = Materia(
        codigo   = "MAT101",
        nombre   = "Cálculo Diferencial",
        creditos = 3,
        docente  = "Ana María Ospina",
        horario  = "Lunes, Miércoles y Viernes  10:00 AM - 11:00 AM"
    )

    bd = Materia(
        codigo   = "INF210",
        nombre   = "Bases de Datos I",
        creditos = 3,
        docente  = "Jorge Andrés Cardona",
        horario  = "Miércoles y Viernes  2:00 PM - 4:00 PM"
    )

    english = Materia(
        codigo   = "ING101",
        nombre   = "Inglés Técnico",
        creditos = 2,
        docente  = "Sandra Milena Torres",
        horario  = "Lunes  6:00 PM - 8:00 PM"
    )

    # Matricular las materias en el estudiante (método de Estudiante)
    estudiante1.matricular_materia(prog1)
    estudiante1.matricular_materia(calculo)
    estudiante1.matricular_materia(bd)
    estudiante1.matricular_materia(english)

    # ─────────────────────────────────────────────────────────
    # PASO 3: Instanciar objetos Nota y registrarlos en cada
    #         materia usando el método agregar_nota()
    # ─────────────────────────────────────────────────────────
    print("\n--- Registrando notas ---")

    # Notas de Programación I (total 100%)
    prog1.agregar_nota(Nota("Taller 1 — Algoritmos",    4.2, 15))
    prog1.agregar_nota(Nota("Primer Parcial",            3.8, 30))
    prog1.agregar_nota(Nota("Proyecto POO (parcial)",   4.5, 25))
    prog1.agregar_nota(Nota("Segundo Parcial",           4.0, 30))

    # Notas de Cálculo Diferencial (total 100%)
    calculo.agregar_nota(Nota("Quiz 1",                  3.5, 10))
    calculo.agregar_nota(Nota("Primer Parcial",          2.8, 35))
    calculo.agregar_nota(Nota("Talleres",                3.2, 20))
    calculo.agregar_nota(Nota("Segundo Parcial",         2.9, 35))

    # Notas de Bases de Datos I (total 100%)
    bd.agregar_nota(Nota("Taller SQL",                   4.8, 20))
    bd.agregar_nota(Nota("Primer Parcial",               4.3, 35))
    bd.agregar_nota(Nota("Proyecto Base de Datos",       4.6, 45))

    # Notas de Inglés Técnico (total 100%)
    english.agregar_nota(Nota("Speaking Test 1",         3.9, 25))
    english.agregar_nota(Nota("Written Exam",            3.5, 40))
    english.agregar_nota(Nota("Final Project",           4.1, 35))

    print("  ✔ Notas registradas correctamente.\n")

    # ─────────────────────────────────────────────────────────
    # PASO 4: Generar el reporte académico completo
    #         Método generar_reporte() del objeto Estudiante
    # ─────────────────────────────────────────────────────────
    estudiante1.generar_reporte()

    # ─────────────────────────────────────────────────────────
    # PASO 5: Demostración con un segundo estudiante
    # ─────────────────────────────────────────────────────────
    print("\n\n--- SEGUNDO ESTUDIANTE ---\n")

    estudiante2 = Estudiante(
        codigo   = "2023-0342",
        nombre   = "Sebastián Morales Herrera",
        carrera  = "Ingeniería de Sistemas",
        semestre = 3,
        email    = "s.morales@umanizales.edu.co"
    )

    prog1_s2 = Materia("INF201", "Programación I",     4,
                       "Carlos Betancourt Correa",
                       "Martes y Jueves  8:00 AM")
    calculo_s2 = Materia("MAT101", "Cálculo Diferencial", 3,
                         "Ana María Ospina",
                         "Lunes, Miércoles y Viernes  10:00 AM")

    prog1_s2.agregar_nota(Nota("Primer Parcial",   2.5, 30))
    prog1_s2.agregar_nota(Nota("Taller 1",         3.0, 20))
    prog1_s2.agregar_nota(Nota("Segundo Parcial",  2.8, 50))

    calculo_s2.agregar_nota(Nota("Primer Parcial", 4.1, 40))
    calculo_s2.agregar_nota(Nota("Talleres",       3.9, 20))
    calculo_s2.agregar_nota(Nota("Final",          4.0, 40))

    estudiante2.matricular_materia(prog1_s2)
    estudiante2.matricular_materia(calculo_s2)

    estudiante2.generar_reporte()


# ─────────────────────────────────────────────────────────────
# Punto de entrada del programa
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
