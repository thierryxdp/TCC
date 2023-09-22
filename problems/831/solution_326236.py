def lingua_p(palavra):
    palavra = palavra.lower()
    lingua_p = ''
    for i in range(len(palavra)-1):
        ligua_p+=palavra[i]
        if palavra[i] in 'aeiou':
            ligua_p+='p'
    return lingua_p