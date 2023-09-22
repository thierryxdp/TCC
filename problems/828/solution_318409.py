def primo(x):
    '''funçao que verifica se dado numero x é primo ou não;
    int->bool'''
    y=0
    for elem in range(1,x+1):
        if x%elem==0:
            y=y+1
        if y==2:
            return True
        else:
            return False