def uppCons(frase):
    '''Recebe uma frase e retorna a frase com todas as consoantes em
    maiúsculas, e o resto dos caracteres iguais aos da frase original.
    
    str -> str'''
    contador = 0
    vogais = 'AEIOUaeiouÁÉÍÓÚáéíóúÃÕãõÂÊÔâêô'

    while contador < len(frase):
        if frase[contador] not in vogais:
            letraMaiuscula = str.upper(frase[contador])
            frase = str.replace(frase, frase[contador], letraMaiuscula)
        contador = contador + 1

    return frase