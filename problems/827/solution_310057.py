def qtd_divisores(x):
    i=1
    s=[]
    while i <=x:
       if x%i==0:   
            s.append(i)
            i+=1
       else:
           
            i+=1
    return len(s)