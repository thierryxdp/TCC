def lingua_p(palavra):
    vogais=['A','E','I','O','U','a','e','i','o','u']
    for i in range(len(palavra)):
        if palavra[i] not in vogais:
            palavra=palavra[:i]+'j'+palavra[i:]
    palavra=str.lower(palavra)
    return palavra