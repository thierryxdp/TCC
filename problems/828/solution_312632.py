def primo(n):
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
    for i in range(2,n):
        if n%1==0 and n%n==0:
            if n%i!=0:
                return True
            else:
                return False