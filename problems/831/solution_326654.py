def lingua_p(palavra):
    vogais=['A','E','I','O','U','a','e','i','o','u']
    for i in range(len(palavra)):
        if palavra[i] in vogais:
            palavra=palavra[:i+1]+'p'+palavra[i+1:]
    return palavra