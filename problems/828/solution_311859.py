def primo(int_Pos):
    divisores = int_Pos
    
    for divisor in range(1,int_Pos+1):
        if (int_Pos % divisor) != 0:
            divisores -= 1
            if (divisores <= 2):
                return True
            else: 
                return False