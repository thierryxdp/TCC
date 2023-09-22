def repetidos(lista_num):
    '''
	Função que retorna o número de vezes que um elemento é igual ao seu anterior, 
    após recebr uma lista de numeros
    list-> int
    '''
    dupla_repetidos = 0
    i = 0
    while i < (len(lista_num)-1):
        if lista_num[i] == lista_num[i+1]:
            dupla_repetidos = dupla_repetidos + 1
        i = i+1
    return dupla_repetidos