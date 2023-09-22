def uppCons(frase:str)-> str:
    """Recebe uma frase e retorna ela com todas as suas consoantes maiúsculas"""
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnçpqrstvxyz':
            frase = frase.replace(frase[i],str.upper(frase[i]))
        i=i+1  
    return frase