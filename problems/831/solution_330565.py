def ligua_p(palavra):
    for i in range(len(palavra)):
        palavranova = list(str.lower(palavra))
        if palavranova[i] in 'aeiou':
            list.insert(palavranova, (i+1), 'p')
        if palavranova[i] not  in 'aeiou':
            palavranova = palavranova + palavranova[i]
    return palavranova