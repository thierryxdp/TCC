def primo(num):
    contador=0
    for d in range(2,num):
        if num%d!=0:
            contador+=1
    return contador