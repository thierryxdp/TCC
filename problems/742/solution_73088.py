def substitui(s,x,i):
    if (0 <= i <= len(s)):
            return ( s[:i] + x + s[i:])
    else:
        return str ("i deve ser um numero inteiro entre 0 e comprimento da string")