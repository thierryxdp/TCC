def lingua_p(palavra):
    alterado=''
    for i in len(palavra):
        if palavra[i] in 'aeiou':
            p_=(palavra[:i] + 'p'+palavra[i:])
        alterado= alterado + p_
    return alterado