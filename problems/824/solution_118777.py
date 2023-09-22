def uppCons(frase):
    '''
    Dado uma frase modifica todos as consoantes minisculas para maisculas.

    Uso:
    uppCons(frase)

    Entrada:
    - frase (list, int): Frase original

    Saída:
    - Retorna a frase com todas suas consoantes em maiúsculas
    (os demais caracteres permanecem como estavam na frase original). (str)
    '''
     i = 0
    frase2 = []
    while i < len(frase):
        if str.lower(frase[i]) in "bcdfghjklmnpqrstvxywzç":
            list.append(frase2, str.upper(frase[i]))
             else:
            list.append(frase2, frase[i])
             i = i + 1
           return str.join("", frase2)