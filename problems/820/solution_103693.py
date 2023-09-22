def posLetra(frase, letra, numero):
    
    qnt_letras = str.count(frase, letra)
    if qnt_letras < n:
        return -1
    else:
        return str.index(frase, letra, p)