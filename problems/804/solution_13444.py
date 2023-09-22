def filtra_pares(tupla):
        if tupla[0] % 2 == 0 and tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
            return tupla[0:3]
        elif tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
            return tupla[1:]
        elif tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
            return tupla[2:]
        elif tupla[3] % 2 == 0:
            return   tupla[3]
        else:
            return ()