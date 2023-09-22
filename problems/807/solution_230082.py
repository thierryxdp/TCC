def conta_frases(texto):
    '''Funcao que dado um texto conta o numeros de frases 
       presentes nesse texto e retorna o resultado.
       Parametros:
       Str
       Saida: int
    '''
    h= str.find(texto, '.')
    i= str.count(texto, '!')
    j= str.find(texto, '...')
    k= str.count(texto, '?')

    return h+i+j+k