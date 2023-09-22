def posLetra(frase, letra, n):
    
    qnt_letras = str.count(frase, letra)
    if qnt_letras < n:
        return -1
    else:
        return str.index(frase, letra, n)
    
    i=0
    p=0
    p2=0
    while i <len(frase):
        p=str.index(frase, letra, p2)