def lingua_p(palavra):
    alterado=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            p=(palavra[:i] + 'p' )
        alterado= alterado + p
    return alterado