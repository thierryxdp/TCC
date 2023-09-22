#
def lingua_p(palavra):
    palavra=list(palavra.lower())
    vogais=['a','e','i','o','u']
    for i in range(len(palavra)):
        if palavra[i] in vogais:
            list.insert(palavra,i+1,'p')
            list.insert(palavra,i+2,palavra[i])
    palavra+=palavra[i]
    return palavra