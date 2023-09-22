def faltante(lista):
    """ Dado uma lista de números inteiros(de 1 até N) com um número a menos, a função retorna o número que está faltando no intervalo da lista;
   list->int"""
    indice=0
    n=1
    while indice<=len(lista):
        if n in lista:
            n=n+1
            indice=indice+1
        else:
            return n