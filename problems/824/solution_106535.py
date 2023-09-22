def uppCons(frase):
    '''Função que recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúscula.
    	str -> str'''
    NovaFrase = " "
    indice = 0
    while indice <len(frase):
        if frase[indice] not in 'AEIOUaeiou':
            NovaFrase= frase[indice].upper
		i=i+1
    return NovaFrase