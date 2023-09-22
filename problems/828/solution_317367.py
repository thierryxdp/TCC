def primo(numero):

    i = 1

    j = []

    while i <= numero:

        if numero%i == 0:

            j  += i

            i += 1

        else:

             i += 1

    if len(j) ==  2:

        return True

    else:

        return False