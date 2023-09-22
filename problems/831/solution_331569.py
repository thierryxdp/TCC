def lingua_p(palavra):
    '''
    	Funcao que recebe uma palavra e retorna esta mesma 
        palavra traduzida para a língua do P
        str -> str
    '''
    palavraCp = ''
    for letra in palavra:
        if letra in 'aeiou':