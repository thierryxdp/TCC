def lingua_p(palavra):
    vogais = ['A','E','I','O','U','a','e','i','o','u']
    palavra = list(palavra)
    index = 0
    quantas_vezes = len(palavra)
    while index <= quantas_vezes+2:
        if palavra[index] in vogais:
            palavra.insert(index+1,'p'+palavra[index])
        index += 1
    
    if palavra[len(palavra)-1] in vogais:
        palavra.insert(len(palavra),'p' + palavra[len(palavra)-1])
    return "".join(palavra)