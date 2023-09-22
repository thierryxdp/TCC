def lingua_p(palavra):
    traducao=' '
    for i in palavra:
        if palavra[i] in "aeiouAEIOU":
            traducao = traducao + palavra[i] + 'p'
        else:
            if palavra[i] not in "aeiouAEIOU":
                traducao = traducao + palavra[i]
    return str.lower(traducao)