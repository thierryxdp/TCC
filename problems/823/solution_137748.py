def faltante(num):
    
    i=0
    x=len(num)+1
    
    soma_todos=sum(x)
    
    soma_num=0
    
    while soma_num<soma_todos:
        
        soma_num=soma_num+num[i]
        i+=1
        
        return soma_todos-soma_num