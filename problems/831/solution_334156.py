def lingua_p(palavra):
    traducao=' '
    for i in palavra:
        if i in "aeiouAEIOU":
            traducao = traducao + palavra[i] + 'p'
        else:
            if i not in "aeiouAEIOU":
                traducao = traducao + palavra[i]
    return str.lower(traducao)