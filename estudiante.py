"""

Archivo    : estudiante.py
Descripción: Define la clase Estudiante, núcleo del sistema.
             Un estudiante tiene materias, genera su reporte
             académico y calcula su rendimiento global.
=============================================================
"""
class Estudiante:
    """
    Clase que representa a un estudiante universitario.

    Centraliza toda la información académica del estudiante:
    datos personales, semestre, carrera y lista de materias cursadas.
    Permite registrar materias, consultar promedios y generar reportes.

    Atributos:
        codigo   (str) : Código estudiantil único.
        nombre   (str) : Nombre completo del estudiante.
        carrera  (str) : Nombre de la carrera que estudia.
        semestre (int) : Semestre actual del estudiante.
        email    (str) : Correo electrónico institucional.
        materias (list): Lista de objetos Materia matriculados.
    """

    def __init__(self, codigo, nombre, carrera, semestre, email):
        """
        Constructor de la clase Estudiante.

        Inicializa todos los datos personales y académicos del estudiante.
        La lista de materias comienza vacía y se llena con matricular_materia().

        Args:
            codigo   (str): Código estudiantil.
            nombre   (str): Nombre completo.
            carrera  (str): Nombre de la carrera.
            semestre (int): Semestre actual.
            email    (str): Correo institucional.
        """
        self.codigo   = codigo
        self.nombre   = nombre
        self.carrera  = carrera
        self.semestre = semestre
        self.email    = email
        self.materias = []   # Lista de objetos Materia

    # ── Métodos de gestión de materias ─────────────────────────────────────

    def matricular_materia(self, materia):
        """
        Agrega una materia a la lista de materias del estudiante.

        Args:
            materia (Materia): Objeto de la clase Materia a matricular.
        """
        self.materias.append(materia)
        print(f"  ✔ Materia '{materia.nombre}' matriculada para {self.nombre}.")

    def buscar_materia(self, codigo):
        """
        Busca una materia por su código.

        Args:
            codigo (str): Código de la materia a buscar.

        Returns:
            Materia | None: El objeto Materia si se encuentra, None si no.
        """
        for materia in self.materias:
            if materia.codigo == codigo:
                return materia
        return None

    # ── Métodos de cálculo académico ───────────────────────────────────────

    def calcular_promedio_general(self):
        """
        Calcula el promedio general del estudiante sobre todas sus materias.

        Sólo incluye materias que tienen al menos una nota registrada.

        Returns:
            float: Promedio general. Retorna 0.0 si no hay materias con notas.
        """
        materias_con_notas = [m for m in self.materias if m.notas]
        if not materias_con_notas:
            return 0.0
        total = sum(m.calcular_promedio() for m in materias_con_notas)
        return round(total / len(materias_con_notas), 2)

    def total_creditos_cursados(self):
        """
        Suma los créditos de todas las materias matriculadas.

        Returns:
            int: Total de créditos académicos cursados.
        """
        return sum(m.creditos for m in self.materias)

    def materias_aprobadas(self):
        """
        Retorna la lista de materias que el estudiante tiene aprobadas.

        Returns:
            list[Materia]: Lista de materias con promedio >= 3.0.
        """
        return [m for m in self.materias if m.esta_aprobada()]

    def materias_reprobadas(self):
        """
        Retorna la lista de materias que el estudiante tiene reprobadas.

        Returns:
            list[Materia]: Lista de materias con promedio < 3.0 y con notas.
        """
        return [m for m in self.materias if m.notas and not m.esta_aprobada()]

    # ── Métodos de visualización ───────────────────────────────────────────

    def mostrar_perfil(self):
        """
        Muestra los datos personales y académicos del estudiante.
        """
        print("=" * 55)
        print("         PERFIL DEL ESTUDIANTE")
        print("=" * 55)
        print(f"  Código      : {self.codigo}")
        print(f"  Nombre      : {self.nombre}")
        print(f"  Carrera     : {self.carrera}")
        print(f"  Semestre    : {self.semestre}°")
        print(f"  Email       : {self.email}")
        print(f"  Materias    : {len(self.materias)}")
        print(f"  Créditos    : {self.total_creditos_cursados()}")
        print("=" * 55)

    def generar_reporte(self):
        """
        Genera e imprime en consola el reporte académico completo
        del estudiante, incluyendo todas las materias y su estado.
        """
        print("\n" + "=" * 55)
        print("       REPORTE ACADÉMICO COMPLETO")
        print("=" * 55)
        print(f"  Estudiante : {self.nombre}  |  Cód: {self.codigo}")
        print(f"  Carrera    : {self.carrera}  |  Semestre: {self.semestre}°")
        print("=" * 55)

        if not self.materias:
            print("  Sin materias registradas.")
            return

        print("\n--- MATERIAS MATRICULADAS ---\n")
        for i, materia in enumerate(self.materias, 1):
            print(f"  [{i}] {materia.nombre} ({materia.codigo})")
            materia.mostrar_info()

        aprobadas  = self.materias_aprobadas()
        reprobadas = self.materias_reprobadas()

        print("--- RESUMEN FINAL ---")
        print(f"  Promedio general  : {self.calcular_promedio_general():.2f} / 5.00")
        print(f"  Materias aprobadas: {len(aprobadas)}")
        print(f"  Materias en riesgo: {len(reprobadas)}")
        print(f"  Créditos totales  : {self.total_creditos_cursados()}")

        if reprobadas:
            print("\n  ⚠ Materias con promedio bajo:")
            for m in reprobadas:
                print(f"     - {m.nombre}: {m.calcular_promedio():.2f}")

        print("=" * 55)
