def primo(numero):
    divisor = 0
    for divisior in range(1, numero):
        if numero % divisor == 0:
            divisor += 1
       elif divisor > 1:
            return 'False'
        else:
            return 'True'