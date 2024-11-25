def es_par(numero):
    """
    Determina si un número es par, manejando entradas no válidas con excepciones.

    Args:
        numero: El número a verificar (debe ser un entero).

    Returns:
        bool: True si el número es par, False si es impar.

    Raises:
        TypeError: Si la entrada no es un número.
    """
    if not isinstance(numero, (int, float)):
        raise TypeError("La entrada debe ser un número.")
    return numero % 2 == 0