def divisores(num):
2	    divisores = 0
3	    for i in range(1, num):
4	        if num % i == 0: 
5	           divisores = divisores + 1
6	    return divisores