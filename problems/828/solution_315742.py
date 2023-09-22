def primo(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(pow(n,0.5)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False