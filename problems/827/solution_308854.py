def qtd_divisores(nume):

    divisores = []

    for dado in range(0, nume+1):

        if nume % dado == 0:

            divisores.append(dado)

    return len(divisores)