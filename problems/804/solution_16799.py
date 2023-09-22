def filtra_pares(tupla):

    a1,a2,a3,a4 = tupla
    tupla2 = a1*(int(a1%2==0)),a2*(int(a2%2==0)),a3*(int(a3%2==0)),a4*(int(a4%2==0))

    if (tupla2[0]!=0) and (tupla2[1]!=0) and (tupla2[2]!=0) and (tupla2[3]!=0):
        return tupla2

    elif (tupla2[0]!=0) and (tupla2[1]!=0) and (tupla2[2]!=0) and (tupla2[3]==0):
        return tupla2[0],tupla2[1],tupla2[2]
    elif (tupla2[0]!=0) and (tupla2[1]!=0) and (tupla2[2]==0) and (tupla2[3]!=0):
        return tupla2[0],tupla2[1],tupla2[3]
    elif (tupla2[0]!=0) and (tupla2[1]==0) and (tupla2[2]!=0) and (tupla2[3]!=0):
        return tupla2[0],tupla2[2],tupla2[3]
    elif (tupla2[0]==0) and (tupla2[1]!=0) and (tupla2[2]!=0) and (tupla2[3]!=0):
        return tupla2[1],tupla2[2],tupla2[3]

    elif (tupla2[0]!=0) and (tupla2[1]!=0) and (tupla2[2]==0) and (tupla2[3]==0):
        return tupla2[0],tupla2[1]
    elif (tupla2[0]!=0) and (tupla2[1]==0) and (tupla2[2]==0) and (tupla2[3]!=0):
        return tupla2[0],tupla2[3]
    elif (tupla2[0]==0) and (tupla2[1]==0) and (tupla2[2]!=0) and (tupla2[3]!=0):
        return tupla2[2],tupla2[3]
    elif (tupla2[0]==0) and (tupla2[1]!=0) and (tupla2[2]!=0) and (tupla2[3]==0):
        return tupla2[1],tupla2[2]
    elif (tupla2[0]==0) and (tupla2[1]!=0) and (tupla2[2]==0) and (tupla2[3]!=0):
        return tupla2[1],tupla2[3]
    elif (tupla2[0]!=0) and (tupla2[1]==0) and (tupla2[2]!=0) and (tupla2[3]==0):
        return tupla2[0],tupla2[2]

    elif (tupla2[0]!=0) and (tupla2[1]==0) and (tupla2[2]==0) and (tupla2[3]==0):
        return tupla2[0],
    elif (tupla2[0]==0) and (tupla2[1]!=0) and (tupla2[2]==0) and (tupla2[3]==0):
        return tupla2[1],
    elif (tupla2[0]==0) and (tupla2[1]==0) and (tupla2[2]!=0) and (tupla2[3]==0):
        return tupla2[2],
    elif (tupla2[0]==0) and (tupla2[1]==0) and (tupla2[2]==0) and (tupla2[3]!=0):
        return tupla2[3],

    else:
        return ()