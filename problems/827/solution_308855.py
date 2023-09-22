def qtd_divisores(nume):

    divisores = []

    for dado in range(1, nume+1):

        if nume % dado == 0:

            divisores.append(dado)

    return len(divisores)