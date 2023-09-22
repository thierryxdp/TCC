def uppCons(frase):
'Função que receba como entrada UMA frase e retorne a frase com todas as suas consoantes maiusculas '''  
s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            s += caractere
    return s

print(consoantes_maiusculas('abcdef')) # aBCDeF