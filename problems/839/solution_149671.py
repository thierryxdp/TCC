def carros(pessoas,cap):
    resto=pessoas%5
    if resto==0:
        return pessoas//5
    else:
        return (pessoas//5)+1