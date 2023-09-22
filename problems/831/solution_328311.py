def lingua_p(palavra):
    '''Função que receba uma palavra de entrada e retorne a 
    	a mesma palavra com a letra p entre vogais. 
        str-->str.'''
    A=" "
    v="aeiou"
    for l in palavra:
        if l in v:
            A=A+(l+"p"+l)
        else:
            A=A+l
    return str.lower(A)