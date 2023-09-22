def conta_frases(s):
    '''Função que dado um texto armazenado em uma string, 
    conta o número de frases que aparecem nesse texto.
    assinatura: str -> int'''
    k=str.replace(s,"...","+")
    ls=str.count(k,".") + str.count(k,"?") + str.count(k,"!") + str.count(k,"+")
    return ls