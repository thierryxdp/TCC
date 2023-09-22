def lingua_p(palavra):
    a=''
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            a+=palavra[i].replace(palavra[i],'p')
    return a