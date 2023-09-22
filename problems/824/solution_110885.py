def uppCons(frase: str) -> str:
    """ recebe uma frase e retorna outra frase com todas as suas consoantes
    em maiúsculas """
    
    total = ''
    i = 0
    
    while i < len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyzç":
            total = total + frase[i].upper()
        else:
            total = total + frase[i]
        i = i + 1
        
    return total