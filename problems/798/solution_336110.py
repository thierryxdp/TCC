# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    i=0
    j=0
    dic={}
    while i<len(frases):
        dic[frases[i]]=0
        i=i+1
    while j<len(frases):
        dic[frases[j]]=dic[frases[j]]+1
        j=j+1
    return dic