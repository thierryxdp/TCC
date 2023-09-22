def eh_quadrada(x):
    k=[]
    for i in range(len(x)):
        k.append(len(x)==x[i])
    if False in k:
        return False
    else:
        return True
        
eh_quadrada([1,2],[2,3])