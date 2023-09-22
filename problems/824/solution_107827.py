def uppCons(frase):
    '''Função que recebe uma frase e retorna a mesma
    com todas as suas consoantes em letra maiusculas e as demais
    letras mantem como estavam anteriormente
    str ->str'''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZzç':
            frase = frase.replace(frase[contador],frase[contador].upper())
        contador += 1
    return frase