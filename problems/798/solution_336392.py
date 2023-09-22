def freq_palavras(frases):
    'dada uma frase retorne um dicionario tendo como chave cada palavra contida nesta frase e como valor a qauntidade de vezes que esta palavra aparece na frase.str-->dict'
    frase=str.split(frases)
    dicio={}
    for i in frase:
        if i not in dicio:
            dicio[i]=1
        else:
            dicio[i]=dicio[i]+1
    return dicio