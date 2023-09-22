def primo(n):
    total_div = 0
    for c in range(1, n + 1):
        if n %c == 0:
            total_div += 1
            
            
            
            
    if total_div == 2:
        return True
    else:
        return False