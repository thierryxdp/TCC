def repetidos(lista):
    nova_lista = lista[::]
    resposta = 0
    contador = 0
    posicao = 0
    while contador < len(lista)-1:
        if lista[contador] == lista[contador+1]:
            resposta += 1
        contador +1    
    return resposta