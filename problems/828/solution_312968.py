def primo(numero):
    """Função que dado um número inteiro positivo, verifica se ele é
    ou não um número primo.
    
    Observação: Um número é primo quando tem apenas dois divisores:
    o número 1 e ele mesmo.
    
    Parameters:
    numero: É o número que será verificado.
    
    Returns:
    Retorna True se o número for primo e False se ele não for.
    int -> bool
    """
    if qtd_divisores(numero) == 2:
        return True
    else:
        return False