def filtra_pares(num):
    """Função que, ao receber uma tupla com quatro elementos inteiros, retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam; tupla->tupla"""
    if(int(num[0])%2 == 0 and int(num[1])%2 == 0 and int(num[2])%2 == 0 and int(num[3])%2 == 0):
        return (num[0],num[1],num[2],num[3])
    elif(int(num[0])%2 != 0 and int(num[1])%2 == 0 and int(num[2])%2 == 0 and int(num[3])%2 == 0):
        return (num[1],num[2],num[3])
    elif(int(num[0])%2 != 0 and int(num[1])%2 != 0 and int(num[2])%2 == 0 and int(num[3])%2 == 0):
        return (num[2],num[3])
    elif(int(num[0])%2 != 0 and int(num[1])%2 != 0 and int(num[2])%2 != 0 and int(num[3])%2 == 0):
        return (num[3],)
    elif(int(num[0])%2 != 0 and int(num[1])%2 != 0 and int(num[2])%2 != 0 and int(num[3])%2 != 0):
        return ()
    elif(int(num[0])%2 == 0 and int(num[1])%2 != 0 and int(num[2])%2 != 0 and int(num[3])%2 != 0):
        return (num[0],)
    elif(int(num[0])%2 == 0 and int(num[1])%2 == 0 and int(num[2])%2 != 0 and int(num[3])%2 != 0):
        return (num[0],num[1])
    elif(int(num[0])%2 == 0 and int(num[1])%2 == 0 and int(num[2])%2 == 0 and int(num[3])%2 != 0):
        return (num[0],num[1],num[2])
    elif(int(num[0])%2 == 0 and int(num[1])%2 != 0 and int(num[2])%2 != 0 and int(num[3])%2 == 0):
        return (num[0],num[3])
    elif(int(num[0])%2 == 0 and int(num[1])%2 != 0 and int(num[2])%2 == 0 and int(num[3])%2 != 0):
        return (num[0],num[2])
    elif(int(num[0])%2 != 0 and int(num[1])%2 == 0 and int(num[2])%2 != 0 and int(num[3])%2 == 0):
        return (num[1],num[3])
    elif(int(num[0])%2 != 0 and int(num[1])%2 == 0 and int(num[2])%2 == 0 and int(num[3])%2 != 0):
        return (num[1],num[2])