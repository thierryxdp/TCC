def primo(x):
    soma=0
    for valor in range(1,x+1):
        if x%valor==0:
            soma=soma+1
    if soma==2:
        return 'true'
    else:
        return 'false'