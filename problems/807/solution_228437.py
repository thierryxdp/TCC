def conta_frases(texto):
    '''função que dado um texto, retorna o número de frase desse texto;str->int'''
    final='.'
    exclamacao='!'
    interrogacao='?'
    reticecias='...'
    frasefinal=str.count(texto,final)
    frasexcl=str.count(texto,exclamacao)
    fraseinter=str.count(texto,interrogacao)
    fraseret=str.count(texto,reticecias)
    return frasefinal+frasexcl+fraseinter+fraseret