def uppCons(frase):
    '''
    	Função que recebe uma frase e retorne 
        a frase com todas as suas consoantes em maiúsculas.
        i:int.
        frase:str
        return:str
        
    '''
    new_frase = ''
    i=0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            M = frase[i].upper()
            new_frase = new_frase + M
        else:
            new_frase = new_frase + frase[i]
        i+=1
    return new_frase