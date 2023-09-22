def faltante(lista):
    """essa função determina, através de um numero inteiro ordenado de 1 a N, qual a peça que está faltando no quebra-cabeças;
    list->list"""
    list.reverse(lista)
    num=lista[0]
    list.sort(lista)
    i=0
    a=0
    while i<num:
        a+=1
        if a!=lista[i]:
            return a
        i+=1
    return i+1