def primo(numero):
    #Vai do 0 até o número
    for divisor in range(numero):
       #verifica se o divisor é diferente de zero
        if divisor != 0 :
            #verifica se não tem um número menor que ele que o divida
            if divisor < numero and divisor !=1 and numero%divisor ==0:
                return False
    return True