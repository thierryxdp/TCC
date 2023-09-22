def busca(setor,matriz):
    """retorna dados dos funcionarios do setor desejado
   str,list[list[str]]->list[str]"""
    dados=[]
    for i in range(len(matriz)):
        dado=[]
        if matriz[i][2]==setor:
            dado.append(matriz[i][0])
            dado.append(matriz[i][1])
            dado.append(matriz[i][3])
        dados.append(dado)
    return dados