def lingua_p(palavra):
    palavra1 = list(palavra)
    palavra_p = []
    for i in  range(len(palavra1)):
        if palavra1[i] in 'aeiouAEIOU':
            list.append(palavra_p, palavra1[i])
            list.append(palavra_p, "p") 
        else:
            list.append(palavra_p, palavra[i])
    list.append(palavra_p, palavra1[len(palavra1)-1])
    a = str.join('', palavra_p)
    return a