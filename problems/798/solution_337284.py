def freq_palavras(frase):
    numero=[]
    contar=0
    dividir=frase.split()
    for c in dividir:
        numero.append(dividir.count(c))
    dicionario=dict(zip(dividir,numero))
    return dicionario