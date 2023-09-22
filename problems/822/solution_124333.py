def repetidos(n: list) -> int:
    
    i = 0
    total = []
    
    while i < len(n):
        
        if n[i] == n[i-1]:
            total = total + [1]
        i = i + 1
        
    return len(total)