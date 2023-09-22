def primo(numero):
    """ verifica se o num é primo e retorna bool ou
    dizendo o que é.. int -> bol, str"""
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                return False
                break
            else:
                return True
    elif numero == 0:
        print(numero, 'é zero')
    elif numero == 1:
         print(numero, 'é um')
    else:
         print(numero, 'é negativo')