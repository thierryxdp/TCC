def isprimo(numero):
    if numero != 0 and numero != 1:
        if numero &gt; 3:
            if numero % 2 == 0 or numero % 3 == 0:
                return False
            else:
                return True
        else:
            return True
    return False