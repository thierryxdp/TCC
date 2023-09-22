def faltante(lista):
    '''Descobre qual o número da peça do quebra-cabeça de Joãzinho
    que está faltando.
    lista -> int'''                    
    indice = 0
    numero_peca = 0
    lista1= list.copy(lista)
    lista_crescente = list.sort(lista1)
    lista2 = list.copy(lista1)
    lista_reversa = list.sort(lista2, reverse = True)
                                     
    while indice <= len(lista) :
        if lista != lista2 or lista[indice+1] - lista[indice] != 1 :
                numero_peca += lista[indice] + 1 
                return numero_peca
        if lista != lista1 or lista[indice] - lista[indice + 1] != 1 or len(lista) == 1:
                numero_peca += lista[indice] - 1  
                return numero_peca
        if lista[0]== 2:
                return 1
        if lista[-1] - lista[-2] == 1:
                numero_peca = lista[indice] + 2
 
                
        indice += 1
    return numero_peca