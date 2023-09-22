def lingua_p(palavra):
    vogal = ["a","e","i","o","u"]
    lista = str.split(palavra)
    for num in range(len(palavra)):
        if lista[num] in vogal:
            lista[num:num] = "p"
            num = num + 1

    return str.join(lista)