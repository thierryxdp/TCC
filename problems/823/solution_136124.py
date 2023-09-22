def faltante(lista):
    ''' a funcao com uma lista com N-1, retorna com o numero que esta faltando no intervalo'''
    x=1
    pecas=[x]
    lista1 = len(lista)+1
    while x< lista1:
        pecas+=[(x+1),]
        x= x+1
    total_1= sum(pecas)
    total_2= sum(lista)
    return total_1 - total_2