def uppCons(fease):
    """recebe uma frase e retorna a frase com todas
    as suas consoantes em maiúscula e o resto como 
    estava. str->str"""
    i=o
    while i<len(frase):
        if frase[i] not in "aeiouAEIOUãáàéèíóôú":
            frase=frase.replace(frase[i],frase[i].upper())
            i=i+1
            return frase