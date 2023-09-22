def conta_frases(texto):
    """A funcao recebe um texto e retorna a quantidade de frases que aparecem nesse texto,
    considerando que cada frase no texto e terminada com um ponto final, um ponto de exclamacao,
    um ponto de interrogacao ou reticencias.
    Parametro de entrada:str
    Valor de retorno: int"""
    if '.' in texto:
        texto=str.replace(texto,"!",".")
        texto=str.replace(texto,"?",".")
        texto=str.replace(texto,"...",".")
        return (len(str.split(texto,".")))-1
    elif '!' in texto:
        texto=str.replace(texto,"?","!")
        texto=str.replace(texto,"...","!")
        return (len(str.split(texto,"!")))-1
    elif '?' in texto:
        texto=str.replace(texto,"...","?")
        return (len(str.split(texto,"?")))-1
    else:
        return (len(str.split(texto,"...")))-1