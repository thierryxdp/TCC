def busca(string, matriz):
    """Dada uma matriz com dados sobre os funcionários de uma empresa
    e uma string relativa a um dos setores da empresa, retorna uma
    lista com os dados dos funcionários do setor;
    string, list -> list"""
    retorno=[]
    for linha in matriz:
        if string in linha[2]:
            retorno.append([linha[0],linha[1],linha[3]])
    return retorno