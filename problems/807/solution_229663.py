def conta_frases(texto):
    """
    Função que dado um texto, retorna o número de frases
    que tem o texto
    string ---> int
    """
    texto1=str.replace(texto,"?",".")
    texto2=str.replace(texto,"!",".")
    texto3=str.replace(texto,"...",".")
    return (str.split(texto3,"."))