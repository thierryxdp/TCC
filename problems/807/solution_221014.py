def conta_frases(frases):
    """funcao que calcula o numero de frases que aparecem em um texto, sendo cada frase terminada com um ponto final, um ponto de exclamaca, ponto de interrogacao ou reticencias;
    str -> int"""
    lista=[]
    if '?' in frases:
        int(str.count(str.replace(frases,'?','.')))=lista[0]
    if '!' in frases:
        int(str.count(str.replace(frases,'!','.')))+=lista[0]
    if '...' in frases:
        int(str.count(str.replace(frases,'...','.')))+=lista[0]
    return int(lista[0])