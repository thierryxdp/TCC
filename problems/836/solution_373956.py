def busca(s,m):
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    lista_vazia=[]
    for i in range(qtd_linhas):
        if m[i]==s:
            lista_vazia.append(i)
    return lista_vazia