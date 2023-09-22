def uppCons(frase):
    '''Função que recebe como entrada uma frase e retorne a frase com todas
       as suas consuantes em maiúculas.
       str ---> str'''
    contador = 0
    resp = []
    letra = []
    while contador < len(frase):
        contador = contador + 1
        if frase[contador] in 'abcdefghijklmnopqrstuxyz':
            letra = str.upper(frase[contador])
        else:
            resp = resp + frase[contador]
    contador = contador + 1
            return resp