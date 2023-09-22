def filtraMultiplos(lista_num,n):
    '''Função que filtra na lista de entrada (lista_num) os números
    múltiplos do número fornecido: n
    	list, float -> list
    '''
    contador = 0
    resposta = list()

    while contador <= len(lista_num):
        if lista_num[contador]%2 == 0:
            resposta += [lista_num[contador],]
        contador += 1
    return lista_num