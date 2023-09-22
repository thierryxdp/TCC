def freq_palavras(frases):
    """recebe uma string e retorna a frequencia das pelavras
    string -> dict"""
    lista={}
    r=frases.split()
    for p in r:
        lista[p]=0
    for p in r:
        if p in lista:
            lista[p]+=1
    return lista