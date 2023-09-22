def lingua_p(palavra):
    """kfmksld"""
    
    palavra = list(palavra.lower())
    i = 0
    for x in palavra:
        if x in "aáãâeéêíioõôúu":
            soma = 'p'+ palavra[i]
            palavra.insert(palavra.index(x,i)+1, soma)
        i += 1
    final = "".join(palavra)
    
    return final