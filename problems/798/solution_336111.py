# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    dic={}
    j=0
    i=0
    while j<len(frases.split()):
        dic[frases.split()[j]]=0
        j=j+1
    while i<len(frases.split()):
        dic[frases.split()[i]]=dic[frases.split()[i]]+1
        i=i+1
    return dic