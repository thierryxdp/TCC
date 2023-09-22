def busca(b,matriz):
    """dada a matriz, busca com base em uma string a coluna da matriz que contem
    essas informacoes, se nao houver nenhum registro retorna lista vazia
    str,list-> list"""
    l=[]
    for c in matriz:
        if c==b:
            l+=c
    return l