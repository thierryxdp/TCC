def primo(int_Pos):
    """Funcão que testa e retorna se um numero inteiro escolhido
    é primo ou não.
    Entrada: int;
    Saida: bool;
    
    Parameters:
    int_Pos: Numero inteiro positivo a ser testado"""
    divisores = int_Pos
    
    for divisor in range(1,int_Pos+1):
        if (int_Pos % divisor) != 0:
            divisores -= 1
    if (divisores <= 2):
        return True
    else: 
        return False