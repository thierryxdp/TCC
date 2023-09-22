def melhor_volta (todos):
    
    final = ()
    a = len(todos)
    b = len(todos[0])
    volta = 0
    
    for i in range(a):
        for j in range(b):
            final = min(todos[j])
            
            volta +=1
    return final