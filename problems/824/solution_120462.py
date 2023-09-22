def uppCons (frase):
    """recebe como entrada uma frase e retorna a frase com todas as suas consoantes emmmaiúsculas (e os demais caracteres exatamente como estavam na frase original)"""
    i=0
    while i<len(frase):
        if texto[i] not in 'AEIOUaeiou':
            frase= str.upper(frase[i])
            i=i+1
    return frase