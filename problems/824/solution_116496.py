def uppCons(frase:str)-> str:
    """Recebe uma frase e retorna ela com todas as suas consoantes maiúsculas"""
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxyz':
            frase[i]=frase.upper(frase[i])
        i=i+1  
    return frase