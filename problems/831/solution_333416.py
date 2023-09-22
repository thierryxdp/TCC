def lingua_p(palavra):
    '''
    	Função que recebe como parâmetro uma palavra, e retorna a mesma palavra com a letra 'p' após qualquer vogal e em seguida
        a vogal novamente.
        str -> str
    '''
    palavra = palavra.lower()
    
    for letra in palavra:
        if letra in 'aeiouáéíóúãõ':
            palavra=palavra.replace(letra,(letra+'p'+letra))
    return palavra