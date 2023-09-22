def uppCons(frase):
    """Função que recebe uma frase e a retorna com todas as suas consoantes
em maiúsculo; str -> str"""
    cont = 0
    frase_nova=""
    while cont<len(frase):
        if str.upper(frase[cont]) in "BCDFGJKLMNPQRSTVWXZ":
            frase_nova+=str.upper(frase[cont])
            cont+=1
        else:
            if str.lower(frase[cont]) in "aeiou":
                frase_nova+=frase[cont]
                cont+=1
    return frase_nova