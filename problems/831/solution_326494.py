def lingua_p(palavra):
    vogais=['A','E','I','O','U','a','e','i','o','u']
    for i in range(len(palavra)):
        if palavra[i] not in vogais:
            palavra=str.replace(palavra,palavra[i],'j')
    palavra=str.lower(palavra)
    return palavra