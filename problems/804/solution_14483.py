def filtra_pares(tupla):
    if tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        tupla1= (tupla[0],tupla[1],tupla[2],tupla[3])
        return tupla1
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2!=0:
        tupla2=(tupla[0],tupla[1],tupla[2])
    	return tupla2
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2!=0 and tupla[3]%2==0:
        tupla3=(tupla[0],tupla[1],tupla[3])
        return tupla3
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2!=0 and tupla[3]%2!=0:
        tupla4=(tupla[0],tupla[1])
        return tupla4
    elif tupla[0]%2==0 and tupla[1]%2!=0 and tupla[2]%2==0 and tupla[3]%2==0:
        tupla5= (tupla[0],tupla[2],tupla[3])
        return tupla5
    elif tupla[0]%2==0 and tupla[1]%2!=0 and tupla[2]%2==0 and tupla[3]%2!=0:
        tupla6=(tupla[0],tupla[2])
        return tupla6
    elif tupla[0]%2==0 and tupla[1]%2!=0 and tupla[2]%2!=0 and tupla[3]%2==0:
        tupla7=(tupla[0],tupla[3])
        return tupla7
    elif tupla[0]%2==0 and tupla[1]%2!=0 and tupla[2]%2!=0 and tupla[3]%2!=0:
        tupla8= (tupla[0])
        return tupla8
    elif tupla[0]%2!=0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        tupla9= (tupla[1],tupla[2],tupla[3])
        return tupla9
    elif tupla[0]%2!=0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2!=0:
        tupla10= (tupla[1],tupla[2])
        return tupla10
    elif tupla[0]%2!=0 and tupla[1]%2==0 and tupla[2]%2!=0 and tupla[3]%2==0:
        tupla11=(tupla[1],tupla[3])
        return tupla11
    elif tupla[0]%2!=0 and tupla[1]%2==0 and tupla[2]%2!=0 and tupla[3]%2!=0:
        tupla12=(tupla[1])
        return tupla12
    elif tupla[0]%2!=0 and tupla[1]%2!=0 and tupla[2]%2==0 and tupla[3]%2==0:
        tupla13= (tupla[2],tupla[3])
        return tupla13
    elif tupla[0]%2!=0 and tupla[1]%2!=0 and tupla[2]%2==0 and tupla[3]%2!=0:
        tupla14= (tupla[2])
        return tupla14
    elif tupla[0]%2!=0 and tupla[1]%2!=0 and tupla[2]%2!=0 and tupla[3]%2==0:
        tupla15= (tupla[3],)
        return tupla15
    elif tupla[0]%2!=0 and tupla[1]%2!=0 and tupla[2]%2!=0 and tupla[3]%2!=0:
        return ()