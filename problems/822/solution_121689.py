def repetidos (lista):
    ''' função que recebe uma lista de números e retorna a
        quantidade de vezes que o número sucessor era igual
        ao número antecessor
        [list-->int]'''
    
    
    indice = 0
    repetições = 0

    while indice < len(lista):
        if   indice != len(lista)-1 and lista[indice] == lista[indice+1]:
            repetições += 1
              
        indice += 1
        
    return repetições