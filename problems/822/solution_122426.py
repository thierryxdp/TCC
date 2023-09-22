def repetidos(list_num):
    lista=[]
    i=0
    
    while i < len(list_num):
        if list_num[i]==list_num[i-1]:
            lista.append(i)
        i+=1
        
    return len(lista)