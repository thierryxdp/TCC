def busca(b,matriz):
    """dada a matriz, busca com base em uma string a coluna da matriz que contem
    essas informacoes, se nao houver nenhum registro retorna lista vazia
    str,list-> list"""
    if matriz==[]:
        return []
    else:
        l=[]
        i=0
        linha=0
        for c in matriz:
            q=0
            i+=1
            for v in c:
                if v==b:
                    linha=i
                    local=c.index(v)
                    l.append(matriz[i-1])
        return l