def uppCons(frase):
    'função que recebe uma frase e a retorna com suas consoantes maiúsculas'
    frase = frase.upper()
    frase = frase.lower('AEIOU')
    return frase