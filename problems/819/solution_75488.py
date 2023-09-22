def filtraMultiplos(lista_num, numero):
    """Funcao que, com base em uma lista dada, retorna os numeros
    existentes na mesma, que sejam multiplos de um numero escolhido,
    em uma nova lista.
   	Entrada: list, int;
    Saida: list;
    
    Parameters:
    lista_num: Lista para ser filtrada
    numero: Numero multiplo
    """
    posicao = 0
    multiplos = []
    while posicao < len(lista_num):
        if lista_num[posicao] % numero == 0 :
            multiplos.append(lista_num[posicao])
        posicao = posicao + 1
    return multiplos