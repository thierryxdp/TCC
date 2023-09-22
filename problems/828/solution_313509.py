def primo(num):
    " " "Dado um número inteiro positivo, verifica se este número é primo ou não, se for retorna True se não False;int, -> Booleans " " "
    mult = 0
    for i in list(range(2, num)):
        if num % i == 0: 
             mult = mult + 1
    if mult == 0:
        return True
    else:
        return False