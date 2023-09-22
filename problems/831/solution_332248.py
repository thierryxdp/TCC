def lingua_p(palavra):
    """Função que recebe uma frase e retorna a mesma traduzida para a língua do P. str -> str"""
    palavra = list(palavra.lower())
    i = 0
    for vogal in palavra:
        if vogal in 'aáéeiúou':
            insere = 'p'+vogal
            palavra.insert(palavra.index(vogal,i)+1,insere)
        i += 1
    palavra_com_p = ''.join(palavra)
    return palavra_com_p