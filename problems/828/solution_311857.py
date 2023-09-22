def primo(int_Pos):
    divisores = int_pos
    
    for divisor in range(1,number+1):
        if (number % divisor) != 0:
            divisores -= 1
            if (divisores <= 2):
                return True
            else: 
                return False