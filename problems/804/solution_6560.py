def filtra_pares(tupla):
    """funcao que retorna apenas os valores pares da tupla"""
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    if a%2==0:
        if b%2==0:
            if c%2==0:
                if d%2==0:
                    return tupla[0],tupla[1],tupla[2],tupla[3]
                else:
                    return tupla[0],tupla[1],tupla[2]

            else:
                if d%2==0:
                    return tupla[0],tupla[1],tupla[3]
                else:
                    return tupla[0],tupla[1]
        else:
            if c%2==0:
                if d%2==0:
                    return tupla[0],tupla[2],tupla[3]
                else:
                    return tupla[0],tupla[2]

            else:
                if d%2==0:
                    return tupla[0],tupla[3]
                else:
                    return tupla[0]
    else:
        if b%2==0:
            if c%2==0:
                if d%2==0:
                    return tupla[1],tupla[2],tupla[3]
                else:
                    return tupla[1],tupla[2]

            else:
                if d%2==0:
                    return tupla[1],tupla[3]
                else:
                    return tupla[1]
        else:
            if c%2==0:
                if d%2==0:
                    return tupla[2],tupla[3]
                else:
                    return tupla[2]

            else:
                if d%2==0:
                    return tupla[3],
                else:
                    return ()