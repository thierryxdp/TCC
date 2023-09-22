def primo (numero):
    """Função que, dado um número inteiro e positivo, retorna se ele é primo ou não.
    Entrada: int.
    Saída: boolean."""
    
    divisores = []
    
    for num in range(1,numero+1):
        if numero%num == 0:
            list.append(divisores, num)
            
    if len(divisores) > 2:
        return False
    else:
        return True