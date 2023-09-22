def uppCons(frase):
    '''
    	Funcao recebe uma string com uma frase
        e retorna a frase com todas as suas consoantes 
        maiusculas (e os demais caracteres como estavam).
        str -> str
        
    '''
    i = 0
    frase = frase.upper()
    while i < len(frase):
        if frase[i] in 'AEIOUÁÉÍÓÚÃÕÂÊÔ':
            frase = frase.replace(frase[i],frase[i].lower(),1)
        i = i + 1
    return frase