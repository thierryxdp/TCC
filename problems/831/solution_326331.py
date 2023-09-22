def lingua_p(palavra):
    """kfmksld"""
    
    palavra = list(palavra.lower())
    i = 0
    for x in palavra:
        if x in "aeiou":
        soma = 'p'+ palavra[i]
        palavra.insert(palavra(x, i)+1, soma)
    final = "".join(palavra)
    return final