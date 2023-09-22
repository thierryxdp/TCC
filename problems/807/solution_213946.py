def contafrases(texto):
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')-str.count(texto,'...')