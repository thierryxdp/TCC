def lingua_p(palavra):
    palavra=str.lower(palavra)
    palavra_p=''
    i=0
    for palavra[i] in palavra:
        if palavra[i]=='aeiou':
            palavra_p+= palavra[i]+'p'+palavra[i]
        i=i+1
    return palavra_p