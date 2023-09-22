def repetidos(lista_numeros):
    '''Função que recebe uma lista de números e retorna o
    número de vezes que um elemento da lista é igual ao 
    elemento anterior
    [list] -> int'''
    i = 0
    numero_ocorrencias = 0
    while i < len(lista_numeros):
        if lista_numeros[i+1] == lista_numeros[i]:
            numero_ocorrencias = numero_ocorrencias + 1
        i = i + 1
    return numero_ocorrencias