def primo(num):
    for divisor in range(1,num):
        if num%divisor==0:
            return False
       	else:
            return True