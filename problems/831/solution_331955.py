def lingua_p(palavra):
    palavra=str.lower(palavra)
    palavra_p=''
    for palavra[i] in palavra:
        if palavra[i]'aeiou':
            palavra_p+= palavra[i]+'p'+palavra[i]
    return palavra_p