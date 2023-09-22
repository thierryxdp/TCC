def conta_frases(texto):
    '''função responsável por contar o número de frases em um texto,(texto),de escolha do usuário'''
    return str.count(texto,'.')+str.count(texto,"!")+str.count(texto,"?")-2*str.count(texto,"...")