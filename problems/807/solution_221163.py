def conta_frases(texto):
    '''função que identifica o número de frases em um texto dado em formato de string;sting->int'''
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'...')-(3*str.count(texto,'...'))