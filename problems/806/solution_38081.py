#Start your python function here
def colisao(ret1,ret2):
    x1=int(ret1[0])##as variaveis transformam cada parte da tupla em 2 coordenadas de um plano
    y1=int(ret1[1])
    x2=int(ret1[2])
    y2=int(ret1[3])
    r1=int(ret2[0])
    q1=int(ret2[1])
    w2=int(ret2[2])
    t2=int(ret2[3])
    if x1==r1 and y1==q1:#se forem iguais eles ocupam o mesmo espaço
        return True
    elif(x1+1)== r1 and (y1+1)==q1:
        return True
    elif x1==r1 and y1>q1:
        return True
    elif(x1+1)>r1 and (y1+1)>q1:
        return False
    elif(x1+1)==r1 and y1>q1:
        return True
    elif x1<=r1 and y1<=q1 and x2>=w2 and y2<=t2:
        return True
    elif x1<r1 and y1<q1 and x2<w2 and y2<t2:
        return False