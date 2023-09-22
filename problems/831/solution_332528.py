def lingua_p(palavra):
    "str->str"
    palavra_p=""
    for i in palavra:
        if i in 'aeiouAEIOU':
            str.lower(palavra+=i+"p")
        else:
            str.lower(palavra+=i)
    return palavra