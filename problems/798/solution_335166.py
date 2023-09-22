# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
#
#
def freq_palavras(frases):
    i=0
    d={}
    p=frase.split()
    while i<len(p):
        d[p[i]]=p.count(p[i])
        i=i+1
    return p