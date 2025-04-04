"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Tomàs Lloret Martínez
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
    def __mul__(self, other):
        """
        Multiplica el vector por otro vector o una constante.

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * 2
        Vector([2, 4, 6])
        >>> v2 * v1
        Vector([4, 10, 18])
        """
        if isinstance(other, (int, float, complex)):
            # Multiplicación escalar
            return Vector(uno * other for uno in self)
        elif isinstance(other, Vector):
            # Multiplicación entre vectores
            if len(self.vector) != len(other.vector):
                raise ValueError("Los vectores no tienen la misma longitud")
            return Vector(uno * otro for uno, otro in zip(self, other))
            # Esta comprensión funciona de la siguiente manera:
            # Creamos un objeto Vector vacío, que iremos llenando con
            # el resultado de multiplicar cada componente de self por
            # el vector other (juntados en la dupla creada por la función zip)
        
    def __rmul__(self, other):
        """
        Método reflejado de la multiplicación
        """
        return self.__mul__(other)
    
    def __matmul__(self, other):
        """
        Método que hace el producto escalar

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        """

        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Los vectores no tienen la misma longitud")
            return sum(uno * otro for uno, otro in zip(self, other))
        else:
            raise TypeError("El operador @ solo se puede usar entre vectores")
    
    def __rmatmul__(self, other):
        """
        Método reflejado del producto escalar
        """
        return self.__matmul__(other)
    
    def __floordiv__(self, other):
        """
        Devuelve la componente tangencial (paralela) de un vector respecto a otro.

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Los vectores no tienen la misma longitud")
            else:
                modulo_v2_cuadrado = sum(uno ** 2 for uno in other)
                if modulo_v2_cuadrado == 0:
                    raise ValueError("El vector de referencia no puede ser el vector nulo.")
                escalar = (self @ other) / modulo_v2_cuadrado
                return Vector(escalar * otro for otro in other)
        else:
            raise TypeError("El operando debe ser un Vector.")
            
        
    def __rfloordiv__(self, other):
        """
        Método reflejado de la componente tangencial
        """
        return self.__floordiv__(other)
    
    def __mod__(self, other):
        """
        Devuelve la componente normal (perpendicular) de un vector respecto a otro.

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Los vectores no tienen la misma longitud")
            else:
                return self - (self // other)
        else:
            raise TypeError("El operando debe ser un Vector.")
        
    def __rmod__(self, other):
        """
        Método reflejado de la componente normal
        """
        return self.__mod__(other)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()