def uppCons(frase:str) -> str:
    '''Recebe uma frase e retorna a frase com todas as consoantes na forma
    maiúscula, deixando os outros caracteres como estavam na original.'''
    i = 0
    
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOU':
            n = str.replace(frase, frase[i], frase[i].upper())
    	i = i+1
    return n