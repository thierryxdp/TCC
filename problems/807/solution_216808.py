def conta_frase(s):
    """
    
    Parametro de ent
    rada: string
    Valor de Saida: int
    """
    f = str.count(s,".")
    r = str.count(s,"!")
    a = str.count(s,"?")
    return f+r+a