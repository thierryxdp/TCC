def primo(num):
    """essa função irá verificar de um determinado número será primo ou não ; int -> int"""
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False