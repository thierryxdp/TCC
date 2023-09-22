def conta_frases(x):
    '''Função que dado uma uma str, retorna a quantidade
    de frases que tem nela
    str -> int'''
    x = str.replace(x,'...','*')
    x =str.replace(x,'.','*')
    x =str.replace(x,'!','*')
    x =str.replace(x,'?','*')
    y = len(str.split(x,'*'))
    return y-1