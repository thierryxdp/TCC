def qtd_divisores(n):
  
    for i in range (1,n):
        if n % i == 0:
            i=i+1
            print (i)
        else:
            n%i !=0
            print (i)