def melhor_volta (todos):
    
    final = []
    volta = 0
    
    for a in todos:
        
        if todos[0]== min(todos):
            V= todos[0]
            final= final+ [0]
        todos[0]+= 1  
        
    for b in V:
        if b== min(V):
            final= final+ [b]
    
    for y in V:

        if V[volta] == min(V):
            final= final+ [volta]
        volta+= 1
        
    return final