def primo(numero):
    
    i = 2
    lista = []
    while i < numero:
        if numero%i == 0:
            lista.append(i)
        i += 1
    if lista == []:
        return True
    else:
        return False