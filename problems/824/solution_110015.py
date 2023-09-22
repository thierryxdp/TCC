def uppCons(frase):
    """retorna a frase com as consoantes maiúsculas
    str -> str"""
    
    vogais=['A','E','I','O','U','a','e','i','o','u']
    con=['b','c','ç','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    
    frase_nova = ''
    for i in frase:
        if i in con:
            frase_nova=frase_nova+i.upper()
        else:
            frase_nova=frase_nova+i
    return frase_nova