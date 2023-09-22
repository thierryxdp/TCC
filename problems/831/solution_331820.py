def lingua_p(palavra):
    '''
    	Funcao que recebe uma palavra e retorna esta mesma 
        palavra traduzida para a língua do P
        str -> str
    '''
    x = palavra.lower()
    palavraCp = ''
    for letra in x:
        if letra in 'aeiouáéíóú':
            palavraCp += letra + 'p' + letra
        else:
            palavraCp += letra
    return palavraCp