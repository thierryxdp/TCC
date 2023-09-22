def busca(setor, matriz):
2
    """ Função que recebe uma matriz com os dados dos
3
    funcionários da empresa e dado o nome do setor da 
4
    empresa, retorna todos os funcionários do mesmo.
5
    Entrada: lista
6
    Saída: lista """
7
    dados = []
8
    for funcionario in matriz:
9
        linha = []    
10
        if setor in funcionario[2]:
11
            list.append(linha,funcionario[0])
12
            list.append(linha,funcionario[1])
13
            list.append(linha,funcionario[3])
14
            dados = dados + [linha]   
15
    return dados