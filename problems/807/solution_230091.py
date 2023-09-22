def conta_frases(texto):
    '''Funcao que dado um texto conta o numeros de frases 
       presentes nesse texto e retorna o resultado.
       Parametros:
       Str
       Saida: int
    '''
    
    j= str.count(texto, '...')
    h= int(str.count(texto, '.')/3)
    i= str.count(texto, '!')
    k= str.count(texto, '?')

    return h+i+j+k