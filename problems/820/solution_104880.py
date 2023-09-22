def posLetra(string, letra, numero):
    cont=0

    cont_numero=0

    while cont<len(string):

        if string[cont]==letra:

            cont_numero = cont_numero +1

            if cont_numero == numero:

                return cont
        cont=cont +1

    return -1