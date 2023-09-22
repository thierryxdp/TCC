def  faltante (lista):
    """ Dado uma lista de inteiros numerados de 1 até n, retorna qual o valor de n está faltando no intervalo.
    entrada lista inteiro -> sainda int."""
   
    faltante = None
   
    list.sort(lista)
    tamanho = len(lista)
   
    i = 1
    while i < tamanho-1:
        if lista[0] != 1:
            faltante = 1
            return faltante
        if (lista[i] != lista[i-1]) or (lista[i] != lista[i+1]):
            falante = lista[i]
            return faltante