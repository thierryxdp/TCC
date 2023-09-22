def primo(n):
    '''Uma função dado um inteiro retornar se é primo ou não
    int -> booleano'''
divisor = 2
    while divisor < n and primo: # equivalente a "div... and é_primo == True:"
        if n % divisor == 0:
            primo = False
        divisor += 1
  
    
    if primo and n != 1: # 1 não é primo
        print True
    else:
        print False