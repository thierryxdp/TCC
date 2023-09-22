def primo(num:int)->bool:
    """Verifica se o número é primo ou não, retornando um valor booleano."""
    sequencia=list(range(1,num))
    for elemento in sequencia:
        if num%elemento==0 and elemento!=1:
            return False
        else:
            return True