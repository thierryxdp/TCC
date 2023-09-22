def busca(setor,matriz):
    resposta= []
    for i in matriz:
        if i[2] == setor:
            resposta.append(i[0:2] + i[3:])
    return resposta