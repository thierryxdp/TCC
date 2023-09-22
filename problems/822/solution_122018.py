def repetidos(lista_num):
    """Funcao que retorna a quantidade de numeros repetidos em uma
    lista dada pelo utilitario.
    Entrada: list;
    Saida: int;
    
    Parameters:
    lista_num: Lista com os numeros a ser verificada.
    """
    posicao = 0
    repeticao = []
    while posicao < len(lista_num):
        if lista_num[posicao] == lista_num[posicao -1]:
            repeticao.append(1)
        posicao = posicao + 1
    return sum(repeticao)