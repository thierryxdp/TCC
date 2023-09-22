def lingua_p(palavra):
    vogais=['A','E','I','O','U','a','e','i','o','u']
    for i in range(1,len(palavra)):
        if palavra[i] in vogais:
            palavra=palavra[:i+1]+'p'+palavra[i+2:]
    palavra=str.lower(palavra)
    return palavra