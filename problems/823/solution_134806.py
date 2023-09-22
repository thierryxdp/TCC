def faltante1(lista):
    """ Dada uma lsita com N-1 inteiros numerados de 1 a N, retorna o número inteiro 
    deste intervalo que está faltando 
    list -> int """
    i = 1
    while i<=max(lista)+1:
        if i not in lista:
            return i