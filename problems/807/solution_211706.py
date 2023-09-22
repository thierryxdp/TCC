def conta_frases(texto):
    '''Retorna a quantidade de frases presentes no texto entregue
    strins -> int'''
    texto= str.split(str.split(str.split(str.split(texto,"."),"!"),"?"),"...")
    return len(texto)