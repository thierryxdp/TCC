def uppCons(frase):
    """Função que recebe uma string e retorna a string com todas as consoantes em maísculas.
    use str -> str : ['Um homem que podia tudo!'] -> UM HoMeM Que PoDia TuDo!"""
    contador = 0
    #A questão não está considerando 'v' como consoante.
    while contador < len(frase):
        if frase[contador] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZzç':
            frase = frase.replace(frase[contador],frase[contador].upper())
        contador += 1
    return frase