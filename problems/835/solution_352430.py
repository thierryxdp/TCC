def melhor_volta(matriz):
    a=[]
    j=0
    for i in matriz:
        j+=1
        a+=[min(i)] 
        k=i[j]
    a=(min(a))    
    return (j,a,k)