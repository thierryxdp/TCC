def fatorial(num):
    i=0
    l=list(range(num-1,0,-1))
    l1=[]
    while i<num:
        if i==1:
            l1=i*num
        if i>1:
            l1=(l1[0])*i
        i=i+1
    return l1