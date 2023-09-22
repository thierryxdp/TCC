def lingua_p(palavra):
    palavra=str.lower(palavra)
    palavra_p= ''
    i=0
    while i < len(palavra):
        if palavra[i] in 'aeiou':
            palavra_p+= palavra[i]+'p'+palavra[i]
        else:
            palavra_p+= palavra[i]
        i=i+1
    return palavra_p