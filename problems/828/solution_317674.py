def primo(numero):
    "int->bool"
    for possi_divi in range(2,numero):
        if numero%possi_divi==0:
            return False
        else: numero%possi_divi!=0
            return True