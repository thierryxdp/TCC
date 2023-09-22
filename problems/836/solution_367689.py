def busca(string,matriz):

    """ Nesta função, que recebe uma matriz e uma string, busca-se pela matriz
        inteira a string. Caso a string se encontre em uma linha da matriz, a
        função retorna a posição 0,1 e 3 para esta linha.
        Estas informações são referentes ao Nome de um funcionário que está no
        setor fornecido pela string, número do registro do funcionário e o
        número de telefone daquele trabalhador. Caso a string não esteja na matriz
        fornecida, retorna-se uma lista vazia
        str,list -> list
    """

    lista_busca_resultante = []

    for pessoa in matriz:
        if pessoa[2] == string:
            matriz_busca = [pessoa[0],pessoa[1],pessoa[3]]
            list.append(lista_busca_resultante,matriz_busca)
            
    return lista_busca_resultante