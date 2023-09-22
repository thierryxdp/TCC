def melhor_volta (todos):
    
    final = ()
    a = len(todos)
    b = len(todos[0])
    volta = 0
    
    for i in range(a):
        for j in range(b):
            volta = min(todos[i][j])
            
            final +=1
    return volta