def repetidos (lista):
    ''' a função recebe uma lista de numeros e retorna o numero de
    vezes que um elemneto da lista é igual ao elemento anterior
    list->int 
    '''
    proximo=0
    repetidas=0
    while (proximo+1) <= len (lista):
        if lista[proximo-1]==lista[proximo]:
            repetidas=repetidas+1
        proximo=proximo+1
    return repetidas