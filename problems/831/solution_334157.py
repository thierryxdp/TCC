def lingua_p(palavra):
    traducao=' '
    for i in palavra:
        if i in "aeiouAEIOU":
            traducao = traducao + i + 'p'
        else:
            if i not in "aeiouAEIOU":
                traducao = traducao + i
    return str.lower(traducao)