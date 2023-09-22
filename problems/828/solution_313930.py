def primo(x):
    divisores = []
    for i in range(2,x):
        if x % i == 0:
            list.append(divisores,i)
    return len(divisores)==0