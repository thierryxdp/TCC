def lingua_p(s):
    """recebe uma palavra em português e retorna esta palavra traduzida para a língua do P, ou seja, após cada vogal da palavra original, coloca-se a sequência de letras 'p' mais a vogal original,ignorando a diferença entre letras minúsculas e maiúsculas;str->str"""
    a=s[:]
    resposta=""
    for indice in range(len(s)):
        if a[indice] in 'AEIOUÁÉÍÓÚáéíóúaeiou':
            resposta=resposta+a[indice]+'p'+a[indice]
        else:
            resposta=resposta+a[indice]
    return resposta