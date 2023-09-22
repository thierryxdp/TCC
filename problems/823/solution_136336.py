def faltante(lista):
    """Dada uma lista de tamanho N-1, a função calcula o número que
    pertence ao intervalo [1,N], mas que não pertence a lista.
    Parametros de Entrada:list
    Retorna: int"""

    list.sort(lista)

    i=0
    auxiliar=1
    
    if lista[-1]< len(lista)+1:
        return len(lista)+1
    
    while i<len(lista):
        if auxiliar != lista[i]:
            return auxiliar
        i=i+1
        auxiliar= auxiliar+1