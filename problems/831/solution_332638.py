def lingua_p(s):
    vogal = ['a','e','i','o','u']
    lista =[]
    for i in range(0,len(s)):
        if (s[i] in vogal) == True:
            lista.append(s[i]+'p'+s[i])
        else:
            lista.append(s[i])
    return ''.join(lista)