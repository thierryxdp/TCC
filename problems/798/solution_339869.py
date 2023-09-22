# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    frases=frases.split()
    ind=0
    dic={}
    while ind<len(frases):
        if frases[ind] in dic:
            dic[frases[ind]]+=1
        else:
            dic[frases[ind]]=1
        ind+=1
    return dic