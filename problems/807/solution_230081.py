def conta_frases(texto):
    '''Funcao que dado um texto conta o numeros de frases 
       presentes nesse texto e retorna o resultado.
       Parametros:
       Str
       Saida: int
    '''
    h= str.find(texto, '.')
    i= str.find(texto, '!')
    j= str.find(texto, '...')
    k= str.find(texto, '?')

    return h+i+j+k