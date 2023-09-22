def busca(setor,matriz):
    "função que recebe um setor (str) e uma matriz e retorna em lista os dados dos funcionários deste mesmo setor"
    resposta = []
    for linha in matriz:
        if linha[2] == setor:
            list.append(resposta,linha)
    return resposta