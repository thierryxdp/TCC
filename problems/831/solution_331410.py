def lingua_p(palavra):
    lingua_p=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            lingua_p = lingua_p + palavra[i] + 'p'
        lingua_p = lingua_p + palavra[i]
    return lingua_p