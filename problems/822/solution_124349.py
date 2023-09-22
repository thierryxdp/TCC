def repetidos(n: list) -> int:
    """ recebe como entrada uma lista de números e retorna o número
    de vezes que um elemento da lista é igual ao elemento anterior """
    i = 0
    total = []
    
    while i < len(n):
        
        if n[i] == n[i-1]:
            total = total + [1]
        i = i + 1
        
    return len(total)