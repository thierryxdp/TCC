def uppCons(frase):
    '''Função que recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúscula.
    	str -> str'''
    NovaFrase = " "
    indice = 0
    tamanhoFrase = len(frase)
    while indice < tamanhoFrase:
        if frase[indice] not in "AEIOUaeiou":
            NovaFrase = NovaFrase + frase[indice].upper()
		indice=indice+1
    return NovaFrase