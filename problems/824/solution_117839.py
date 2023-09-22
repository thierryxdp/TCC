def uppCons(frase):
    '''funcao que recebe consoantes e vogais em uma frase, e
    	retorna as consoantes em maiusculas e as vogais em 
        minusculas
        frase-> str
        return: str
    '''
    contador = 0
    fraseNova = ''
    while contador < len(frase):
        if frase[contador] not in 'aeiouãéíóú':
            fraseNova += frase[contador].upper()
        else:
            fraseNova += frase[contador].lower()
        contador += 1
        return fraseNova