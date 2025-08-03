# algoritmos_busqueda.py

def busqueda_secuencial(lista, valor):
    """
    Búsqueda secuencial simple.
    Recorre la lista de izquierda a derecha.
    Retorna el índice si se encuentra, o -1 si no.
    """
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


def busqueda_binaria(lista, valor):
    """
    Búsqueda binaria.
    Requiere que la lista esté ordenada.
    Retorna el índice si se encuentra, o -1 si no.
    """
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
