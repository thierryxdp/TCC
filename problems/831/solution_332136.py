def lingua_p(palavra):
    ''' função que ao receber uma palavra (em português) retorna a mesma palavra na língua do P
        lingua do P = após cada vogal da palavra original, é inserida uma sequência de letras 'p'
        mais a vogal original.
        str ---> str'''
    a = palavra
    i = 0
    str.lower(palavra)
    while i < len(palavra):
        if palavra[i] in 'aeiou':
            vogal_com_p = palavra[i] + 'p' + palavra[i]
            a = str.replace(a, palavra[i], vogal_com_p)
            i += 1
        else:
            i +=1
    return a