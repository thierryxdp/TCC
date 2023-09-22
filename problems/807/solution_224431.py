def conta_frases(frase):
    """ Insira um texto entre aspas e a função retornara o numero de frases no texto"""
    ponto=frase.count(".")
    excl=frase.count("!")
    inter=frase.count("?")
    ret=frase.count("...")
    total=ponto+excl+ret+inter
    if ret >=1:
        return total - ret*3
    else:
        return total