def lingua_p(palavra):
    palavra=str.lower(palavra)
    pf=''
    vogais='aeiouáéíóúã'
    for i in palavra:
        pf=pf+i
        if i in vogais:
            pf=pf+'p'+i
    return pf