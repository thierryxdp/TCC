def primos(n):
    multiplos=0
    for i in range(2,n):
        if n % i == 0:
            multiplo +=1
        if multiplo==0:
            return True
        if n%3==0:
            return False