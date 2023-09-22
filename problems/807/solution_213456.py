def conta_frases(a):
    '''Dado um texto armazenado em uma string, 
    retorna a quantidade de frases do texto.
    str --> int'''
    b= str.replace(a,'...',">")
    return str.count(a,'.')+str.count(a,'!')+str.count(a,'?')+str.count(a,b)