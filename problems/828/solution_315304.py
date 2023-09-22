def primo(num):
    for divisor in range(1,num):
        divisores=0
        if num%divisor==0:
            divisores=divisores+1
        if divisores<=2:
            return True
        else:
            return False