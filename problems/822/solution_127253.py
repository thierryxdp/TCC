def repetidos(lista_num):
    '''  Função retorna o número de vezes que um elemento 
    aparece repetido. list -->int'''
    i = 1
    num_vezes = 0
    while len(lista_num) > i:
        if lista+num[i] == lista_num[i-1]:
            num_vezes += 1
            i += 1
        else:
            i += 1
    return num_vezes