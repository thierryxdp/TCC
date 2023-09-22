def faltante(lista):
    """ Dada uma lsita com N-1 inteiros numerados de 1 a N, retorna o número inteiro 
    deste intervalo que está faltando 
    list -> int """
    faltante = sum(range(min(lista), max(lista)+1)) - sum(lista)
    if faltante==0:
        if min(lista)!=1:
            return 1
        return max(lista)+1
    return faltante