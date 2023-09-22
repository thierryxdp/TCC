def lingua_p(palavra):
    for i in len(palavra):
        if i in 'AEIOUaeiou':
            str.replace(palavra[i],palavra[i]+"p"+palavra[i])