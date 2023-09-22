def uppCons(frase):
    """retorna a frase com as consoantes maiúsculas
    str -> str"""
    
    vogais=['A','E','I','O','U','a','e','i','o','u']
    
    
    for i in frase:
        if i not in vogais:
            frase.upper(i)
        return frase