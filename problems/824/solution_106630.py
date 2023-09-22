def uppCons(frase):
    '''recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas
    string -> strin'''
    novaFrase = ""
    i = 0
    while i < len(frase):
        if i not in 'aeiouAEIOU':
            str.upper(i)
        novaFrase = novaFrase + str(i)
        i = i + 1
    return novaFrase