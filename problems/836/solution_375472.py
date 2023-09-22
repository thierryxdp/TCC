def busca(setor,matriz):
    """Função que dada uma matriz e um setor de uma empresa, diz quais são os contatos na matriz que fazem parte desse setor. str , list -> list"""
    resultado_busca = []
    for s in range (len(matriz)):
        if setor in matriz[s]:
            matriz[s].pop(2)
            resultado_busca.append(matriz[s])
    return resultado_busca