def uppCons(frase):
    '''funcao que recebe consoantes e vogais em uma frase, e
    	retorna as consoantes em maiusculas e as vogais em 
        minusculas
        frase-> str
        return: str
    '''
    contador = 0
    novaFrase = ''
    while contador < len(frase):
        if frase[contador] not in 'aeiouãéíóú':
            novaFrase += frase[contador].upper()
        else:
            novaFrase += frase[contador].lower()
        contador += 1

    return novaFrase