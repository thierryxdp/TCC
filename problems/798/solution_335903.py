# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(a):
    dicio={}
    for x in a:
        dicio[x]= str.count(a,x)
    return dicio