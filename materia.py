"""

Archivo    : materia.py
Descripción: Define la clase Materia que modela una asignatura
             dentro del sistema académico.
=============================================================
"""


class Materia:
    """
    Clase que representa una materia o asignatura universitaria.

    Modela los atributos de una asignatura que cursa un estudiante,
    incluyendo su código, nombre, créditos, docente y horario de clase.

    Atributos:
        codigo  (str): Código único de la materia (ej. "INF101").
        nombre  (str): Nombre completo de la materia.
        creditos(int): Número de créditos académicos.
        docente (str): Nombre del docente a cargo.
        horario (str): Días y hora de la clase (ej. "Lunes y Miércoles 8:00 AM").
    """

    def __init__(self, codigo, nombre, creditos, docente, horario):
        """
        Constructor de la clase Materia.

        Inicializa todos los atributos de la materia al momento de su creación.

        Args:
            codigo   (str): Código único de la materia.
            nombre   (str): Nombre completo de la materia.
            creditos (int): Número de créditos académicos.
            docente  (str): Nombre del docente a cargo.
            horario  (str): Días y hora de la clase.
        """
        self.codigo   = codigo
        self.nombre   = nombre
        self.creditos = creditos
        self.docente  = docente
        self.horario  = horario
        self.notas    = []   # Lista de objetos Nota registrados en esta materia

    def agregar_nota(self, nota):
        """
        Agrega una nota a la lista de notas de la materia.

        Args:
            nota (Nota): Objeto de la clase Nota a registrar.
        """
        self.notas.append(nota)

    def calcular_promedio(self):
        """
        Calcula el promedio ponderado de todas las notas registradas.

        Multiplica cada nota por su porcentaje y suma los resultados.

        Returns:
            float: Promedio ponderado. Retorna 0.0 si no hay notas.
        """
        if not self.notas:
            return 0.0
        total = sum(n.valor * (n.porcentaje / 100) for n in self.notas)
        return round(total, 2)

    def esta_aprobada(self):
        """
        Determina si la materia está aprobada con base en el promedio.

        Returns:
            bool: True si el promedio es mayor o igual a 3.0, False en caso contrario.
        """
        return self.calcular_promedio() >= 3.0

    def mostrar_info(self):
        """
        Muestra la información completa de la materia en consola,
        incluyendo las notas registradas y el promedio.
        """
        estado = "APROBADA" if self.esta_aprobada() else "EN CURSO / REPROBADA"
        print(f"  Código    : {self.codigo}")
        print(f"  Materia   : {self.nombre}")
        print(f"  Créditos  : {self.creditos}")
        print(f"  Docente   : {self.docente}")
        print(f"  Horario   : {self.horario}")
        if self.notas:
            print(f"  Notas     :")
            for nota in self.notas:
                print(f"              {nota.descripcion}: {nota.valor} "
                      f"({nota.porcentaje}%)")
            print(f"  Promedio  : {self.calcular_promedio():.2f}  →  {estado}")
        else:
            print(f"  Notas     : Sin notas registradas aún.")
        print()
