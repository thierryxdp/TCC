def busca(setor, matriz):
    '''
    Função que recebe um setor especifico de uma empresa
    e matriz com dados dos seus funcionários (inclusive 
    o setor) e retorna os dados dos funcionários do setor 
    '''
    resposta = []
    for n in matriz:
        if n[2] == setor:
            resposta.append(n[0:2] + n[3:])
    return resposta