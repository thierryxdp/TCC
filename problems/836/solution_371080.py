def busca (setor,matriz):
    dados_setor=[]
    for setor_buscado in range(len(matriz)):
        if str.lower(setor) in str.lower(matriz[setor_buscado][2]):
            list.append(dados_setor,matriz[setor_buscado])

    return dados_setor