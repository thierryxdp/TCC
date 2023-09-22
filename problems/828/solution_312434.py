def primo (numero):
    for contador in range(2,numero):
        if (numero % contador) == 0:
            return  "False"
    return "True"