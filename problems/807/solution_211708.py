def conta_frases(texto):
    '''Retorna a quantidade de frases presentes no texto entregue
    strins -> int'''
    t=str.split(texto,"...")
    t=str.split(t,".")
    t=str.split(t,"!")
    t=str.split(t,"?")
    return len(t)