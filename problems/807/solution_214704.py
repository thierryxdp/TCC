def conta_frases(frase):
    """funcao que da um texto ele retorna a quantidade de frases qeu ha nesse texto.
    str->int"""
    a=str.find(frase,".")
    b=str.find(frase,"...")
    c=str.find(frase,"!")
    d=str.find(frase,"?")
    return a+b+c+d