def repetidos(lista_de_numeros):
    '''Função que retorna o número de vezes que um elemento é igual ao elemento anterior, dado a lista de números; list->int'''
    quant_de_iguais=0
    indice=1
    while indice<len(lista_de_numeros):
        if lista_de_numeros[indice-1]==lista_de_numeros[indice]:
            quant_de_iguais=quant_de_iguais+1
        indice=indice+1
    return quant_de_iguais