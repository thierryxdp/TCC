def faltante(lista):
    '''
    funcao que verifica se alguma peca esta faltando do jogo
    e retorna a peca faltante
    lista -> int
    '''
    lista.sort()
    contador = 0
    peca = -1
    
    while contador < len(lista):
        if lista[contador] == contador +1:
            contador +=1
        else:
            peca = contador + 1
            contador = len(lista)
    if peca == -1:
        peca = len(lista)+1
        
    return peca