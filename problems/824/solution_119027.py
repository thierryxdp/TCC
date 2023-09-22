def uppCons(frase):
    """Recebe uma frase e retorna as consoantes da frase maiúsculas.
    Assinatura: str -> str"""
    frasefinal=''
    num=0
    while num<len(frase):
        if frase[num] in "bcdfghjklmnpqrstvwxyz":
            frasefinal+=str.upper(frase[num])
        else:
            frasefinal+=frase[num]
        num+=1
    return frasefinal