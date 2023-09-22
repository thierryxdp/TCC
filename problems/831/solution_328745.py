def lingua_p(palavra):
    palavra1 = list(palavra)
    palavra_p = []
    for i in  range(len(palavra1)):
        if palavra1[i] in 'aeiouAEIOU':
            list.append(palavra_p, palavra1[i])
            list.append(palavra_p,'p')
            list.append(palavra_p, palavra[i])
        else:
            list.append(palavra_p, palavra[i])
    a = str.join('', palavra_p)
    return a