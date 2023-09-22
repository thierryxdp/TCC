def uppCons(frase):
    '''Função que reebe uma frase e retorna a frase com todas as suas consoantes 
    em maiúsculo; str -> str''' 
    cont = 0
    result = ""

    while cont < len(frase):
        if frase[cont] in "bcdfghjklmnpqrstvwxz":
            result +=  frase[cont].upper()
        else:
            result +=  frase[cont]

        cont += 1

    return result