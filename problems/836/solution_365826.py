def busca(setor,matriz):
    '''retorna todos os dados dos funcionários do setor buscado que se 
    encontram na matriz:
    str, list(list) -> list'''
    dados = []
    for funcionario in matriz:
        if funcionario[2] == setor:
            del funcionario[2]
            list.append(dados,funcionario)
    return dados