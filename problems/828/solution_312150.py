def primo(n):
    lista = [n]
    for i in range(1,n):
        if n%i==0:
            lista += [i]
            if len(lista)==2:
                primo = 0
            else:
                primo = 1
    return bool(primo)