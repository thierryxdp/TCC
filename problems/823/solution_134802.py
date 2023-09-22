def faltante(lista):
    """ Dada uma lsita com N-1 inteiros numerados de 1 a N, retorna o número inteiro 
    deste intervalo que está faltando 
    list -> int """
    return sum(range(min(lista), max(lista)+1)) - sum(lista)