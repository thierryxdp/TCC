def filtra_pares(t1):
    """Função que recebe uma string(s), um caractere(x) e um numero(i) entra 0 e o comprimento da string
    retornando, a string "s", sendo trocado o elemento da posição "i" pelo caractere "x";
    str, str, int -> str"""
    if int(len(0)%2) == 0 and not int(len(1,2,3)%2) == 0:
        return s[0] 
    elif int(len(1)%2) == 0 and not int(len(0,2,3)%2) == 0:
        return s[1]
    elif int(len(2)%2) == 0 and not int(len(0,1,3)%2) == 0:
        return s[2]
    elif int(len(3)%2) == 0 and not int(len(0,1,2)%2) == 0:
        return s[3]
    elif int(len(0)%2) == 0 and int(len(1)%2) == 0:
        return s[0,1]
    elif int(len(0)%2) == 0 and int(len(2)%2) == 0:
        return s[0,2]
    elif int(len(0)%2) == 0 and int(len(3)%2) == 0:
        return s[0,3]
    elif int(len(1)%2) == 0 and int(len(2)%2) == 0:
        return s[1,2]
    elif int(len(1)%2) == 0 and int(len(3)%2) == 0:
        return s[1,3]
    else:
        return s[2,3]