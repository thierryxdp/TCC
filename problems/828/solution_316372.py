def primo(num:int)->bool:
    """Verifica se o número é primo ou não, retornando um valor booleano."""
    x = True 
    for i in (2, num):
            while x:
               if num%i == 0:
                   x = False
               else:
                   x = True