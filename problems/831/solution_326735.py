def lingua_p(palavra):
    vogal = "AEIOUaeiou"
    x = len(palavra)
    lingua = ""
    for contador in range(x):
        if palavra[contador] in vogal:
            converter = palavra[contador] + "p" + palavra[contador]
            lingua += converter
            
    return lingua