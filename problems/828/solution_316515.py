def primo(num):
    from math import sqrt
    if(num > 1):
        for i in range(2, sqrt(num)):
            if num%i==0:
                return "False"
            else:
                return "True"
    else:
        return "False"