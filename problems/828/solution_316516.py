def primo(num):
    if num == 2:
        return "True"
    if num % 2 == 0 or num <= 1:
        return "False"
    for i in range(2, num**(1/2)):
        if num%i==0:
            return "False"
        else:
            return "True"