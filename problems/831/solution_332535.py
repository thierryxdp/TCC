def lingua_p(palavra):
    "str->str"
    palavra_p=""
    for i in palavra:
        if i in 'aeiouAEIOU':
            palavra_p+=i+"p"+i
        else:
            palavra_p+=i
    return str.lower(palavra_p)