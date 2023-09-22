def lingua_p(palavra):

    palavram = str.lower(palavra)
    letras = list(palavram)
	x = 0
    for i in letras:
        if i  in ['a','e','i','o','u']:
            pos = list.index(letras,i)
            list.insert(letras,pos+1,'p')
            list.insert(letras,pos+2,i)
            
    junta_letras = "".join(letras)
    return junta_letras