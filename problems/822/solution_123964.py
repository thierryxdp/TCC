def repetidos(lista):
    ''' Função que retorna a quantidades de números iguai ao seu antecessor na lista
 	list -> int '''
    i = 1
    resposta = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            resposta = resposta + 1
            i = i+1
        else:
            i = i+1
    return resposta