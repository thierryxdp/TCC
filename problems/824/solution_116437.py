def uppCons(frase):
    "recebe uma frase e retorna ela com as suas consoantes em maiusculo"
    "entrada: Str. Saida:Str."
    x = ''
    for letra in frase:
        if letra in 'bcçdfghjklmnpqrstvxwyz':
            x += letra.upper() 
        else: 
            x += letra
    return x