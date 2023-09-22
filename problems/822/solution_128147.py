def repetidos(lista):
    '''funcao que retorna a quantidade de vezes que um elemento aparece repetido;
       list=>int'''
    contador = 1
    vezes = 0
    
    while len(lista) > contador:
        if lista[contador] == lista[contador-1]:
            vezes = vezes+1
            contador = contador+1
        else:
            contador= contador+1
    return vezes