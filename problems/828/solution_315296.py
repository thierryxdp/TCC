def primo(n):
    """Função que dado um número n, diz se 
    ele é primo ou não; int -> bool """
    
    divisores = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
              break
    if divisores > 1:
      return False
    else:
      return True