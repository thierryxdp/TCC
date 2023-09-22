def primo (num):
    """Essa função irá verificar se um determinado número é primo ou não ; int -> int"""
    soma = 0
    for c in range(2, num):
        if num % c == 0:
            soma = soma + 1
        else:
            soma = soma
    if soma == 0:
        return 'É número primo'
    else:
        return 'Não é primo'