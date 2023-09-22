def busca(setor, matriz):
2
    """Função que recbe uma matriz com os dados dos 
3
    dos funcionários de uma empresa e dado o setor,
4
    retorna quais funcionários trabalham nela
5
    Entrada : str, list
6
    Saída: list """
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