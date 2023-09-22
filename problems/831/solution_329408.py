def lingua_p(palavra):
    """recebe uma palavra e traduz essa para a lingua do
    p, adicionando um p + a vogal original apos todas 
    as vogais dessa.
    str -> str"""
    copia=[]
    for letra in palavra:
        if letra in "AEIOUaeiou":
            list.append(copia,palavra)
    for verdes in copia:
        str.replace(palavra,verdes,(verdes+"P"+verdes))
    return str.lower(palavra)