def filtraMultiplos(ls,n):
    """ a""" 
    final=[]
    num=0
    while num<len(ls):
        if ls [num]%n==0:
            final.append(ls[num])
        num+=1
    return final