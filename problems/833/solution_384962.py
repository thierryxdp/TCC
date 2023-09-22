def busca(setor, matriz):
    """ Função que dado um número inteiro e uma matriz de
    números inteiros, conta e retorna a quantidade de vezes
    que aquele número aparece na matriz.
    Entrada: lista
    Saída: int """
    dados = []
    for funcionario in matriz:
        linha = []    
        if setor in funcionario[2]:
            list.append(linha,funcionario[0])
            list.append(linha,funcionario[1])
            list.append(linha,funcionario[3])
            dados = dados + [linha]   
    return dados