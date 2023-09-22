def lingua_p(palavra):
    palavra = palavra.lower()
    palavra_p = []
    
    for i in palavra:
        if i in "aãáàâeéèêiíìîoóòôuúùû":
            palavra_p.append(i+"p"+i)
        else:
        	palavra_p.append(i)
    palavra_p = (''.join(palavra_p))
    return palavra_p