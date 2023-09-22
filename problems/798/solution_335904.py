# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(a):
    lista=str.split(a,' ')
    dicio={}
    for x in lista:
        dicio[x]= list.count(lista,x)
    return dicio