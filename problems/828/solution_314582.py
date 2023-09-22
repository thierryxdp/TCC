def primo(n):
    '''retorna True para um n primo ou False para um n não primo; int -> bool'''
    samara = 0
    for i in range(n+1):
        if i == 0:
            samara = samara + 0
        elif n%i == 0:
            samara = samara + 1
    if samara == 2:
        return True
    else:
        return False