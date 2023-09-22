def filtramultiplos(l,n):
    '''it returns just the multiples of n in list
    list,int ->list'''
    multiples=[]
    index=0
    while index<=len(l):
        if l[index]%n==0:
            multiples+= l[index]
        index +=1
    return multiples