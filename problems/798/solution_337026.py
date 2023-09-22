# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """"""
    separada=str.split(frases)
    contador=0
    dic={}
    while contador<len(separada):
        qntd=0
        qntd=list.count(separada,separada[contador])
        map={separada[contador]:qntd,}
        dic[separada[contador]]=qntd
        contador+=1
    return dic