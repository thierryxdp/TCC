def uppCons(frase):
    """ Faça uma função que receba como entrada uma frase e
 retorna a frase com todas as suas consoantes em maiúsculas
 (e os demais caracteres iguais a entrada original)"""
    vowels = ["a","e","i","o","u"]
    count = 0
    len_frase = len(frase)
    new_frase = ""

    while count < len_frase:

        if frase[count] not in vowels:
            new_frase += frase[count].upper()
        
        else:
            new_frase += frase[count]
        count += 1
    return new_frase