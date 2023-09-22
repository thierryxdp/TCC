def lingua_p(palavra):
    palavra = palavra.lower()
    lingua_p = ''
    for i in range(len(palavra)-1):
        lingua_p+=palavra[i]
        if palavra[i] in 'aeiou':
            lingua_p+='p'
    return lingua_p