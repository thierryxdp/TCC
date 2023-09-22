# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frases):
    m = frases.split()
    d={}
    for palavra in m:
        if palavra in d:
            d[palavra]+=1
        else:
            d[palavra]=1
    
    return d