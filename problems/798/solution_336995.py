def freq_palavras(frases):
    """Retorna quantas vezes cada palavras apareceu na frase.(str->dict)"""
    palavras=frases.split()
    contagem={}
    for i in palavras:
        n=list.count(palavras,i)
        contagem[i]=n
    return contagem