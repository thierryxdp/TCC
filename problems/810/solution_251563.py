def inverte(frase):
    '''Retorna a frase com as palavras na ordem inversa, sem pontuação e letras maiúsculas
    str -> str'''
    
    k=";.,-!?"
    i=0
    
    while i<len(frase):
        if frase[i] in k:
            str.replace(frase,frase[i],'',1)
        i=i+1
    
    s=str.split(frase,' ')
    
    str.sort(s,reverse=True)
    
    p=str.join(' ',s)
    
    return p