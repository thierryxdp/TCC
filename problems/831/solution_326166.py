def lingua_p(palavra):
    str.lower(palavra)
    posicao=0
    for posicao in range(len(palavra)):
        vogal=palavra[posicao]
        if vogal in 'aáàãâéeêíiôoúu':
            palavra=palavra.replace(vogal,vogal+'p'+vogal)
            return palavra