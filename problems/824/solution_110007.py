def uppCons(frase):
    """retorna a frase com as consoantes maiúsculas
    str -> str"""
    
    vogais=['A','E','I','O','U','a','e','i','o','u']
    cosoantes=['B','C','D','F','G','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    
    frase_nova = []
    
    for i in frase:
        if i in vogais:
            frase_nova.append(i)
        if i not in vogais:
            frase_nova.append(str.upper(i))
            return ''.join(frase)