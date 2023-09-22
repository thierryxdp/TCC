def lingua_p(palavra):
    min_palavra = list(str.lower(palavra))
    pos = 0
    for vogal in min_palavra:
        if vogal in 'aeiou':
            list.insert(min_palavra,[pos],'p')
        pos = pos + 1
    return str.join('',(min_palavra))