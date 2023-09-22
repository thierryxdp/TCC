def primo(n):
    """Função que dado um numero inteiro positivo, verifica se esse numero é primo
    ou não, e retorna um valor booleano;
    int -> bool"""
    numerosPrimos = 0
    for i in range(1, n + 1):
        if n % i == 0:
            numerosPrimos += 1
            
    if numeorsPrimos == 2:
        return True
    
    else:
        return False