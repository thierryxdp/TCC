def lingua_p(palavra):
    for i in palavra:
        if i in 'AEIOUaeiou':
            palavra[0:(i+1)]+'p'+str(i)+palavra[(i+4):]
    return palavra