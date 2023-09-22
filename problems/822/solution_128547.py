def repetidos (numeros):
    '''função em que dada uma lista de números , e retorne o número de vezes que
    um elemento da lista é igual ao elemento anterior;
    list -> int'''
    i=1
    qtd=0
    while i<=len(numeros):
        if numeros[i]==numeros[(i-1)]:
            qtd=qtd+1
        i=i+1
    return qtd