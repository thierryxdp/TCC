def freq_palavras(frase):
    pal=frase.split()
    dicio={}
    i=0
    j=0
    while i < len(pal):
        dicio[pal[i]]=pal.count(pal[i])
        i=i+1
    return dicio# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis