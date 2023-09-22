def posLetra(texto,letra,n):
    nt=str.join("*",texto)
    lt=str.split(nt,"*")
    if letra in texto:
        if n==1:
            return str.index(texto, letra)