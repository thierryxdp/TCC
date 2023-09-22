def qtd_divisores(num):
    
    i=0
    div=()
    
    for divisores in num:
        if divisores % i == 0:
            div=div + divisores
    		i=i+1
            
    return len(div)