def lingua_p(palavra):
    palavra_com_p = []
    for i in palavra:
        if i in 'aeiou':
            palavra_com_p += i+'p'+i
        else:
            palavra_com_p += i
    return palavra_com_p