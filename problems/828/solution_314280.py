def primo(num):
    """Função que dado um número, determina-se se é primo ou não;
    int -> bool"""
    del listaDivisores
    listaDivisores = []
    listaNum = list(range(1, num +1))
    for i in listaNum:
        if num % i == 0:
            listaDivisores = listaDivisores + [num]
            
        if len(listaDivisores) == 2:
             return True
        else:
             return False