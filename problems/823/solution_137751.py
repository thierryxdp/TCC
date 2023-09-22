def faltante(num):
    
    i=0
    x=len(num)+1
    y=range(1,x)
    
    soma_todos=sum(y)
    
    soma_num=0
    
    while soma_num<soma_todos:
        
        soma_num=soma_num+num[i]
        i+=1
        
        return soma_todos-soma_num