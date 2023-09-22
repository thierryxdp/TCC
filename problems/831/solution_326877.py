def lingua_p(palavra):
    i = 0
    nova_palavra=''
    while (i < len(palavra)):
        if  (str.lower(palavra[i]) in 'aeiou'):
            nova_palavra += palavra[0:i+1] +'p'+palavra[i]
        i += 1
    return nova_palavra