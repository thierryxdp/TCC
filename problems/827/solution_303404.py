def qtd_divisores(num):
    x=1
    div=0
    count=0
    while x<=num:
        if x%div==0:
            count=count+1
        	x=x+1
        div=div+1
    return count