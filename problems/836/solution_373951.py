def busca(s,m):
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    lista_vazia=[]
    for i in m:
        if m[i]==s:
            lista_vazia.append(i)
    return lista_vazia