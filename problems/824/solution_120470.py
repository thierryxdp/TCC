def uppCons (frase):
    """recebe como entrada uma frase e retorna a frase com todas as suas consoantes emmmaiúsculas (e os demais caracteres exatamente como estavam na frase original)"""
    i=0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            fraseindice=frase[i]
            frase[i]=str.upper(fraseindice)
        i=i+1
    return frase