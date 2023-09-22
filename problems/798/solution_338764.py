# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    
    dc = {}
    ls = frases.split()
    for x in ls:
        i=0
        for y in ls:
            if x==y:
                i=i+1          
        d ={x:i}
        dc = {**dc, **d}
    return dc