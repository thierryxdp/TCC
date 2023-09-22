def lingua_p(palavra):
    vogal = "AEIOUaeiouáéíóú"
    x = len(palavra)
    lingua = ""
    for contador in range(x):
        if palavra[contador] in vogal:
            converter = palavra[contador] + "p" + palavra[contador]
            lingua += converter
        else:
            lingua = lingua + palavra[contador]
    return lingua