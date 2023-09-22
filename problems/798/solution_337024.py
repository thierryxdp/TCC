# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """"""
    separada=str.split(frases)
    contador=0
    while contador<len(separada):
        qntd=list.count(separada,separada[contador])
        dic={separada[contador]:qntd}
        contador+=1
    return dic