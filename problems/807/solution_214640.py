def conta_frases(texto):
    '''a função retorna o número de frases que existe em um determinado texto
    entrada:str
    saída:int'''
     x = str.replace(texto,'...','@')
    return str.count(x,'.')+str.count(x,'!')+str.count(x,'?')+str.count(x,'@')