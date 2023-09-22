def faltante(lista):
    '''descobre qual o numero inteiro do intervalo da lista que está faltando'''
    lista.sort()
    inteiroFaltante=0
    i=0
    
    while i in range(len(lista)):
        if(len(lista) == 1):
            inteiroFaltante = lista[i] - 1
            return inteiroFaltante
        elif(i == len(lista)):
           	inteiroFaltante = lista[i] + 1
            return inteiroFaltante
        elif(lista[i + 1] - lista[i] > 1):
            inteiroFaltante = lista[i] - 1
            return inteiroFaltante
        i = i+1