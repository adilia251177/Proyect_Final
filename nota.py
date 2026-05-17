"""

Proyecto   : Sistema de Gestión Académica Estudiantil

=============================================================
"""
class Nota:
    """
    Clase que representa una calificación o nota académica.

    Cada nota está asociada a una actividad evaluativa (parcial, taller,
    proyecto, etc.) y tiene un valor numérico y un porcentaje del total.

    Atributos:
        descripcion (str)  : Nombre de la actividad (ej. "Primer Parcial").
        valor       (float): Calificación obtenida (escala 0.0 a 5.0).
        porcentaje  (int)  : Peso de esta actividad en la nota final (%).
    """

    def __init__(self, descripcion, valor, porcentaje):
        """
        Constructor de la clase Nota.

        Valida que el valor esté entre 0.0 y 5.0, y que el porcentaje
        esté entre 1 y 100.

        Args:
            descripcion (str)  : Nombre o descripción de la actividad.
            valor       (float): Calificación entre 0.0 y 5.0.
            porcentaje  (int)  : Porcentaje que representa en la nota final.

        Raises:
            ValueError: Si el valor o el porcentaje están fuera de rango.
        """
        if not (0.0 <= valor <= 5.0):
            raise ValueError(
                f"El valor de la nota debe estar entre 0.0 y 5.0. "
                f"Se recibió: {valor}"
            )
        if not (1 <= porcentaje <= 100):
            raise ValueError(
                f"El porcentaje debe estar entre 1 y 100. "
                f"Se recibió: {porcentaje}"
            )

        self.descripcion = descripcion
        self.valor       = valor
        self.porcentaje  = porcentaje

    def es_aprobatoria(self):
        """
        Determina si la nota es aprobatoria (>= 3.0).

        Returns:
            bool: True si la nota es mayor o igual a 3.0.
        """
        return self.valor >= 3.0

    def mostrar(self):
        """
        Imprime la información de la nota en consola.
        """
        estado = "✓ Aprobada" if self.es_aprobatoria() else "✗ Reprobada"
        print(f"  Actividad  : {self.descripcion}")
        print(f"  Nota       : {self.valor:.1f} / 5.0  ({self.porcentaje}%)  →  {estado}")
