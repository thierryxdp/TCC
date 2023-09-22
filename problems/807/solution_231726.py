def conta_frases(frase):
    i=frase.count("?")
    e=frase.count("!")
    ret=frase.count("...")
    p=frase.count(".") - 3*ret
    return i+e+ret+p