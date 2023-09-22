def freq_palavras(frase):
    contar=[]
    dividir=frase.split()
    for c in dividir:
        contar += str(dividir.count(c))
    dicionario=dict(zip(dividir,contar))
    return dicionario