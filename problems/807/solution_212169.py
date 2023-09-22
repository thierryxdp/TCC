def conta_frases(texto):
    '''Função que conta e retorna o número de frases presentes em um texto(texto).
       parâmetro de entrada: str
       valor de retorno: int'''
    return str.count(texto,'!')+ str.count(texto,'?')+((str.count(texto,'.')+str.count(texto,'...'))-3*str.count(texto,'...'))