# Busca Funcionários
def busca(busca, matriz):
    '''Ao receber uma matriz com os dados dos funcionários de uma empresa
    e um setor da empresa, a função retorna todos os dados cadastrados
    dos funcionários desse setor;
    STRING, LIST -> LIST'''
    retorno = []
    for i in matriz:
        for j in i:
            if str.lower(busca) in str.lower(j):
                retorno.append(i)
    return retorno