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
        return (E4)
    elif lista=='0010':
        return (E3)
    elif lista=='0100':
        return (E2)
    elif lista=='1000':
        return (E1)
    elif lista=='0011':
        return (E3,E4)
    elif lista=='0101':
        return (E2,E4)
    elif lista=='1001':
        return (E1,E4)
    elif lista=='0110':
        return (E2,E3)
    elif lista=='1010':
        return (E1,E3)
    elif lista=='1100':
        return (E1,E2)
    elif lista=='1110':
        return (E1,E2,E3)
    elif lista=='0111':
        return (E2,E3,E4)
    elif lista=='1011':
        return (E1,E3,E4)
    elif lista=='1101':
        return (E1,E2,E4)
    elif lista== '1111':
        return (e1,e2,e3,e4)
    elif lista=='0000':
        return ()