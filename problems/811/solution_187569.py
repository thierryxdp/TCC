def colchao(medidas, H, L):
    '''funcao que permite comparar se colchao
    passa pela porta de Joao
    entrada: lista, inteiro
    saida: booleano
    '''
    if medidas[1]<=H:
        return 'True'
    elif medidas[2]<=H:
        return 'True'
    elif medidas[1]<=L:
        return 'True'
    elif medidas[2]<=L:
        return 'True'
    else:
        return 'False'