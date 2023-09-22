# Cdef freq_palavras(frases):
    dicio={}
    lista=str.split(frases)
    for x in lista:
        if x in dicio:
            dicio[x]=dicio[x]+1
        else:
            dicio[x]=1
    return dicio
loque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis