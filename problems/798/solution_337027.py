def freq_palavras(frases):
    """funcao que dada uma string retorna quantidade de cada palavra; str->dict"""
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