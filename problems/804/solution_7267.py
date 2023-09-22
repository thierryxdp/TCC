#Start your python function here
filtra_pares(tupla):
    e1=str(int(tupla[0]%2))
    e2=str(int(tupla[1]%2))
    e3=str(int(tupla[2]%2))
    e4=str(int(tupla[3]%2))
    lista=e1+e2+e3+e4
    if lista=='0001':
        return (e4)
    elif lista=='0010':
        return (e3)
    elif lista=='0100':
        return (e2)
    elif lista=='1000':
        return (e1)
    elif lista=='0011':
        return (e3,e4)
    elif lista=='0101':
        return (e2,e4)
    elif lista=='1001':
        return (e1,e4)
    elif lista=='0110':
        return (e2,e3)
    elif lista=='1010':
        return (e1,e3)
    elif lista=='1100':
        return (e1,e2)
    elif lista=='1110':
        return (e1,e2,e3)
    elif lista=='0111':
        return (e2,e3,e4)
    elif lista=='1011':
        return (e1,e3,e4)
    elif lista=='1101':
        return (e1,e2,e4)
    elif lista== '1111':
        return (e1,e2,e3,e4)
    elif lista=='0000':
        return ()