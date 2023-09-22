def primo(numero):
     if numero % numero == 0 and numero % (numero - 1) != 0 and numero % 2 != 0 and numero % 5 != 0 and numero % 11 != 0 and numero % 3 != 0 and numero % 13 != 0:
             return 'True'
     else:
             return 'False'