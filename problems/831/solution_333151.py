def lingua_p(palavra):
    p = ''
    for l in palavra:
        if str.lower(l) in 'aeiouáàãâéèêíìîóòõôúùû':
            p += l + 'p' + l
        else:
            p += str.lower(l)
    return p


lingua_p('advirdes')