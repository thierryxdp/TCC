def faltante(lista):
    '''Essa função ao receber como valor de entrada uma lista com N - 1 inteiros numerados de 1 a N, descobre qual é o número inteiro deste intervalo está faltando.'''
    '''list -> int'''
    i=1
    pecas=[i]
    while i<len(lista)+1:
        pecas+=[(i+1),]
        i+=1
        totalpecas= sum(pecas)
        totalfaltante= sum(lista)
        return totalpecas-totalfaltante