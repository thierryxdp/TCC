def faltante(lista):
    '''descobre qual o numero inteiro do intervalo da lista que está faltando'''
    lista.sort()
    inteiroFaltante=0
    i=0
    
    while i in range(len(lista)):
        if(i == len(lista) - 1):
           	inteiroFaltante = i + 2
        elif(lista[i + 1] - lista[i] > 1):
            inteiroFaltante = lista[i] - 1
        i = i+1
    return inteiroFaltante