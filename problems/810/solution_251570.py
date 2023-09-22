def inverte(frase):
    '''Retorna a frase com as palavras na ordem inversa, sem pontuação e letras maiúsculas
    str -> str'''
    
    k=";.,!?-"
    i=0
    alfa=''
    
    while i<len(frase):
        if frase[i] not in k:
            alfa=alfa+frase[i]
        if frase[i]=='-':
            alfa=alfa+' '
        i=i+1
                        
        
    s=str.split(alfa,' ')
    
    list.reverse(s)
    
    p=str.lower(str.join(' ',s))
    
    return p