def uppCons(frase):
    '''Função que recebe a frase e altera para maiúscula 
    todas as consoantes da frase dada e o restante da frase 
    permanece da mesma forma.
    str -> str'''
    vogal='AEIOUaeiouÃÍÉãíé'
    cons='bcdfghjklmnpqrstvxzwy'
    i=0
    while i<len(frase):
        if frase[i] in 'AEIOUaeiouÃÍÉãíé':
            vogal=vogal+frase[i]
        if frase[i] in cons:
            nf=frase[i].upper()
            vogal=vogal+nf
        i=i+1
    return vogal