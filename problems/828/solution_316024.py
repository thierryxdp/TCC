def primo(num):
    for numeros in range(1,num+ 1):
        if num % numeros == 0: 
            return False
        else:
            return True