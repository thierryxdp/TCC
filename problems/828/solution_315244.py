def primo(numero):
    lista = []
    i = 1
    while i < numero:
        if numero%i==0:
            lista = lista + [i]
        i = i + 1
    if lista == [1,numero]:
        return 'é primo'