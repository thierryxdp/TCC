def faltante(lista):
    """Função que dada uma lista com N-1 inteiros, descobre qual número deste
    intervalo está faltando
   list --> int"""
    
    list.sort(lista)
    i=1
    fim = lista[-1]+1
    while i <= fim:
        if i not in lista:
            return i