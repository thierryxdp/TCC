def primo(num):
    som=0
    for n2 in range(2,num):
        if num%n2==0:
            som=som+1
    if som > 0 :
        return False

    else:
        return True