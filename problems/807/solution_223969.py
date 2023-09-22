def conta_frases(texto):
    '''diz quantas frases existem em um determinado texto'''
    #str -> int
    interrogacao=str.count(texto,'?')
    final=str.count(texto,'.')
    exclamacao=str.count(texto,'!')
    3*'.'=reticencias
    reticencias=str.count(texto,'...')
    return interrogacao+final+exclamacao+reticencias