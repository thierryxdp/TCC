def melhor_volta(A):
    C=[]
    for i in range(6):
        for j in range(10):
            list.append(C,A[i][j])
            P=min(C)
    if (C.index(P)+1)<=10:
        return C.index(P)+1,P,1
    if 10<(C.index(P)+1)<=20:
        return (C.index(P)+1)-10,P,2
    if 20<(C.index(P)+1)<=30:
        return (C.index(P)+1)-20,P,3
    if 30<(C.index(P)+1)<=40:
        return (C.index(P)+1)-30,P,4
    if 40<(C.index(P)+1)<=50:
        return (C.index(P)+1)-40,P,5
    if 50<(C.index(P)+1)<=60:
        return (C.index(P)+1)-50,P,6