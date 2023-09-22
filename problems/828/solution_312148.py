def primo(n):
    lista = []
    for i in range(1,n):
        if n%i==0:
            lista += [i]
            if len(lista)>2:
                primo = 1
            else:
                primo = 0
    return bool(primo),lista