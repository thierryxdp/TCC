def busca(setor,M):
    linha=0
    dados=[]
    for i in M:
        if setor in M[linha]:
            dados_f=M[linha][0]+M[linha][1]+M[linha][3]
            list.append(dados,dados_f)
    linha+=1
    return dados