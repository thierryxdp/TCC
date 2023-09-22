def lingua_p(s):
    """recebe uma palavra em português e retorna esta palavra traduzida para a língua do P, ou seja, após cada vogal da palavra original, coloca-se a sequência de letras 'p' mais a vogal original,ignorando a diferença entre letras minúsculas e maiúsculas;str->str"""
    a=s[:]
    for indice in range(len(s)):
        if a[indice] in 'AEIOUaeiou':
            a[indice]=str(a[indice])+'p'+str(a[indice])
    return a