# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    a=str.split(frases)
    dic={}
    for i in range(len(a)):
        dic[a[i]]=dict.get(dic,a[i],0)+1
    return dic