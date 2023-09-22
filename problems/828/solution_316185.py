def primo(num):
    primos = []
    i=1
    while i <= num:
        if num%i == 0:
            list.append(primos, i)
        i=i+1
    if len(primos) > 2:
        return False
    if len(primos) == 2:
        return True