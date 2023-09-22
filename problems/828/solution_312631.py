def primo(n):
    contador=1
    if n==1:
    	return False
    elif n%2==0:
        return False
    elif n%3==0:
        return False
    elif n%4==0:
        return False
    elif n%5==0:
        return False
    elif n%6==0:
    	return False
    elif n%7==0:
        return False
    for i in range(1,n+1):
        if n%i==0:
            contador+=1
            if contador>2:
                return False
            else:
                return True