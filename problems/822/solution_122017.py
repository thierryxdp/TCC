def repetidos(lista):
    '''funcao que retorna a quantidade de vezes que um elemento
    dentro de uma lista é igual ao anterior
    list->int'''
    soma=0
    i=1
    while i<len(lista):
        if lista[i]==lista[i-1]:
            soma=soma+1
        i=i+1
    return soma