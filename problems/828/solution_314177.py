def primo(n):
    """Função que retorna True se um número n é primo ou False se não for 
int -> bool"""

    total = 0

    for elemento in range(1, n + 1):
        if n % elemento == 0:
            total = total + 1
    if total == 2:
        return True
    else:
        return False