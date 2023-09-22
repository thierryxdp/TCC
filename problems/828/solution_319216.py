def primo(numero):
    "função que verifica se um número qualquer é primo"
    divisor = 0
    contagem = 0
    while contagem <= numero:
        if contagem > 0:
            if numero% contagem == 0:
                divisor += 1
        contagem += 1
    if divisor == 2:
        return True
    else:
        return False