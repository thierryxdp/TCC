def lingua_p(palavra):
    palavra=str.lower(palavra)
    pf=''
    for i in palavra:
        pf=pf+i
        if i in 'aáãâeéêiíoóôõuú':
            pf=pf+'p'+i
    return pf