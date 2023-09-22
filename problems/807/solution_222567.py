def conta_frases(texto):
    '''
    	Função que recebe uma string com um 
        texto armazenado e retorna a 
        quantidade de frases que esse texto 
        possui
        : param texto: str
        : return: int
    '''
    return (str.count(texto,'.') - 3*str.count(texto,'...')) + str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...')