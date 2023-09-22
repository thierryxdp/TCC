def filtraMultiplos(lista, n):
    """Função que dado uma lista e um número, retorna os numeros da lista que são divisiveis pelo numero passado"""
    """list, int -> list"""
    i = 0
    novaLista = []
    while i < len(lista):
        if (lista[i] % n) == 0:
            novaLista.append(lista[i])
        i=i+1
    return novaLista