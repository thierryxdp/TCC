#Start your python function here
def filtra_pares (tupla):
    e1=(int(tupla[0])
    e2=(int(tupla[1])
    e3=(int(tupla[2])
    e4=(int(tupla[3])
    E1=str(k1)
    E2=str(k2)
    E3=str(k3)
    E4=str(k4)
    k1=e1%2
    k2=e2%2
    k3=e3%2
    k4=e4%2
    lista=E1+E2+E3+E4
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