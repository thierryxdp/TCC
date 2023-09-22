def melhor_volta(A):
    C=[]
    for i in range(6):
        for j in range(10):
            list.append(C,A[i][j])
            P=min(C)
    if (C.index(P)+1)<=10:
        return 1,P,C.index(P)+1
    if 10<(C.index(P)+1)<=20:
        return 2,P,(C.index(P)+1)-10
    if 20<(C.index(P)+1)<=30:
        return 3,P,(C.index(P)+1)-20
    if 30<(C.index(P)+1)<=40:
        return 4,P,(C.index(P)+1)-30
    if 40<(C.index(P)+1)<=50:
        return 5,P,(C.index(P)+1)-40
    if 50<(C.index(P)+1)<=60:
        return 6,P,(C.index(P)+1)-50