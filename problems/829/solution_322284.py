def soma_h(numero):
    """realiza uma soma h:int->float"""
    x=1
    h=0
    lista=[]
    while x<=numero:
        h+=1/x
        x=x+1
    return round(h,2)