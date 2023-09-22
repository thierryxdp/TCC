def lingua_p(palavra):
    min_palavra = list(str.lower(palavra))
    pos = 0
    for vogal in min_palavra:
        if min_palavra[pos] in 'aeiou':
            list.append(min_palavra,vogal+'p'+vogal)
        pos = pos + 1
    return str.join('',(min_palavra))