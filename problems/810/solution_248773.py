def inverte(frase):
    frase1= str.join(' ', str.split(frase, '.'))
    frase2= str.join('', str.split(frase1, ','))
    frase3= str.join(' ', str.split(frase2, '?'))
    frase4= str.join(' ', str.split(frase3, '!'))
    frase5= str.join(' ', str.split(frase4, '-'))
         
        todo= frase5.split(' ')
        inver = todo[-1:-(len(todo)+1):-1]
        final = str.strip(str.join(' ',inver))
    
    return str.lower(final)