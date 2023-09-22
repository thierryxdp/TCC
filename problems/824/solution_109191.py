def uppCons(frase):
    'função que recebe uma frase e a retorna com suas consoantes maiúsculas'
    frase = frase.upper()
    frase = frase.replace('A', 'a')
    frase = frase.replace('E', 'e')
    frase = frase.replace('I', 'i')
    frase = frase.replace('O', 'o')
    frase = frase.replace('U', 'u')
    return frase