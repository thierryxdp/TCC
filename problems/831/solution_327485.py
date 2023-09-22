def lingua_p(palavra):

    palavram = str.lower(palavra)
    letras = list(palavram)

    for i in letras:
        if i  in ['a','e','i','o','u']:
            list.insert(letras,i+1,'p')
            list.insert(letras,i+2,i)
            i += +3
        else:
            i += +1
    junta_letras = "".join(letras)
    return junta_letras