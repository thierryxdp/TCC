def filtra_pares(t1):
    """Função que recebe uma string(s), um caractere(x) e um numero(i) entra 0 e o comprimento da string
    retornando, a string "s", sendo trocado o elemento da posição "i" pelo caractere "x";
    str, str, int -> str"""
    if len(0)%2 == 0 and not len(1,2,3)%2 == 0:
        return s[0] 
    elif len(1)%2 == 0 and not len(0,2,3)%2 == 0:
        return s[1]
    elif len(2)%2 == 0 and not len(0,1,3)%2 == 0:
        return s[2]
    elif len(3)%2 == 0 and not len(0,1,2)%2 == 0:
        return s[3]
    elif len(0)%2 == 0 and len(1)%2 == 0:
        return s[0,1]
    elif len(0)%2 == 0 and len(2)%2 == 0:
        return s[0,2]
    elif len(0)%2 == 0 and len(3)%2 == 0:
        return s[0,3]
    elif len(1)%2 == 0 and len(2)%2 == 0:
        return s[1,2]
    elif len(1)%2 == 0 and len(3)%2 == 0:
        return s[1,3]
    else:
        return s[2,3]