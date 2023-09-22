def lingua_p(palavra):
    '''retorna a palavra fornecida traduzida para a 
    lingua do p, em minusculas; str -> str'''
    palavraMin=str.lower(palavra)
    for a in palavraMin:
        palavraMin.replace('a','apa')
    for e in palavraMin:
        palavraMin.replace('e','epe')
    for i in palavraMin:
        palavraMin.replace('i','ipi')
    for o in palavraMin:
        palavraMin.replace('o','opo')
    for u in palavraMin:
        palavraMin.replace('u','upu')
    return palavraMin