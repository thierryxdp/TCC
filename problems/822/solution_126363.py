def repetidos(lista_numeros):
    '''Função que recebe uma lista de números como entrada e retorna
    o número de vezes que um elemento da lista é igual ao elemento anterior;
    lista->int'''
    i=0
    qtd_de_vezes=0
    while i<len(lista_numeros):
            if i!=0 and lista_numeros[i]==lista_numeros[i-1]:
                qtd_de_vezes+=1
            i+=1
    return qtd_de_vezes