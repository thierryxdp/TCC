#Start your python function here
def filtra_pares (tupla):
    e1=(int(tupla[0]))%2
    e2=(int(tupla[1]))%2
    e3=(int(tupla[2]))%2
    e4=(int(tupla[3]))%2
    E1=str(e1)
    E2=str(e2)
    E3=str(e3)
    E4=str(e4)
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