def uppCons(frase):
    """Função que receba como entrada uma frase e retorne a frase com todas as suas consoantes em maiúsculas
    (e os demais caracteres exatamente como estavam na frase original)."""
    i=0
    frase_consoante=[]
    while i<len(frase):
        if not frase[i] in "aeiouáéíóúàèìòùãõâêîôû":
            list.append(frase_consoante,str.upper(frase[i]))
        else:
            list.append(frase_consoante,frase[i])
        i=i+1
    return str.join("",frase_consoante)