def primo(n):
    cont = 0
    div = []
    for i in range(n):
        if n%(i+1) == 0:
            cont += 1
            div.append(i+1)
        else:
            cont
    if cont == 2:
        print (True)
    else:
        print (False)