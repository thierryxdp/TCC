def lingua_p(palavra):
    '''função que retorna uma frase com um P adcionado a vogal anterior'''
    vogal = ['a','e','i','o','u','á','ã','â','ê','é','í','î','õ','ó','ô','û','ú']
    palavranova = []
    for index in range (0,len(palavra)):
        list.append(palavranova,palavra[index])
    ind = 0
    for vezes in range(0,len(palavranova)):
        if palavranova[ind] in vogal:
            list.insert(palavranova, ind + 1, 'p' + str(palavranova[ind]))
            ind = 2 + ind
        else:
            ind  = 1 + ind
    return str.join('',palavranova)