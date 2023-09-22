'''função que recebe dimensões do colchão e medidas de uma porta, e retorna se é possível passar nela'''
def colchao(medida,h,l):
    [a,b,c]=medida
    result=bool
    if medida [0] <= l and medida [1]<=h:
        result= True 
    elif medida [1]<= l and medida[0]<= h:
        result= True
    elif medida [0]<= l and medida [2] <=h:
        result= True
    else:
        result= False
    return result