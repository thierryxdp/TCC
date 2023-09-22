def freq_palavras(frase):
    """Dado uma frase qualquer, retorna a frequência das palavras na
    frase:
    str-->dict"""
    palavra=frase.split()
    lista=[]
    for palavras in palavra:
        lista+=[(palavras,palavra.count(palavras))]
    return dict(lista)