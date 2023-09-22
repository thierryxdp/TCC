def uppCons(phrase):
    """ Faça uma função que receba como entrada uma frase e
 retorna a frase com todas as suas consoantes em maiúsculas
 (os demais caracteres iguais a entrada original)"""
    vowels = ["a","e","i","o","u"]
    count = 0
    len_phrase = len(phrase)
    new_phrase = ""

    while count < len_phrase:

        if phrase[count] not in vowels:
            new_phrase += phrase[count].upper()
        
        else:
            new_phrase += phrase[count]
        count += 1
    return new_phrase