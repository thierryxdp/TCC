def uppCons(frase):
    '''recebe uma frase e retorna a mesma frase com todas as consoantes
       em maiusculas
       str -> str'''
    
    lista=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    a=len(lista)
    x=0
    str.split(frase,'')
    
    while x<a:
        if lista[x] in frase:
            str.replace(frase, lista[x], str.upper(lista[x]))
        x=x+1
    return str.join(frase)