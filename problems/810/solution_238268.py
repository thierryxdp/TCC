def inverte(frase):
    sinal = "!,.@?-"
    for remover in sinal:
        frase = frase.replace(remover," ")
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(' ',lista)
    return str.lower(frase)