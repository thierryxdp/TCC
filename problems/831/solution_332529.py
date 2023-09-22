def lingua_p(palavra):
    "str->str"
    palavra_p=""
    for i in palavra:
        if i in 'aeiouAEIOU':
            palavra+=i+"p"
        else:
            palavra+=i
    return str.lower(palavra)