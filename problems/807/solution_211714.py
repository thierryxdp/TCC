def conta_frases(texto):
    '''Retorna a quantidade de frases presentes no texto entregue
    strins -> int'''
   	n=str.count(texto,".")
    n=str.count(texto,"...")+n
    n=str.count(texto,"!")+n
    n=str.count(texto,"?")+n
    return n