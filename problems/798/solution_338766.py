# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    
    d={}
    for x in frases:
        i=0
        for y in frases:
            if x == y:
                i=i+1
        d[x:i]
    return d