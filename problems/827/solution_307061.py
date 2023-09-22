def qtd_divisores(num):
    
    i=0
    div=()
    
    for i in range(1, num//2+1):
        if num % i == 0:
            div=div + (num)
    		i=i+1
            
    return len(div)