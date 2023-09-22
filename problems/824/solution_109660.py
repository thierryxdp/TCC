def uppCons(frase:str) -> str:
    '''Recebe uma frase e retorna a frase com todas as consoantes na forma
    maiúscula, deixando os outros caracteres como estavam na original.'''
    i = 0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOU':
            frase[i].upper()
    	i = i+1
    return frase[1].upper()