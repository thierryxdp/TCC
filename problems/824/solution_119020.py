def uppCons(frase):
    """Recebe uma frase e retorna as consoantes da frase maiúsculas.
    Assinatura: str -> str"""
    num=0
    while num<len(frase):
        if frase[num] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            str.upper(frase[num])
        num+=1
    return frase