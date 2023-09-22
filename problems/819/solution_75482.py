def filtraMultiplos(lista_num, numero):
    posicao = 0
    multiplos = []
    while posicao < len(lista_num):
        if lista_num[posicao] % numero == 0 :
            multiplos = multiplos + lista_num[posicao]
        posicao = posicao + 1
    return multiplos