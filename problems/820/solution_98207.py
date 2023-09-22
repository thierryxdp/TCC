def posLetra(fragmento,letra,numero) : 
    """Retorna em que posição da string a ocorrência dela 
    está localizada, exemplo : ("dinheiro","i",2) onde está 
    o segundo "i" na palavra "dinheiro";
    str, str, int -> int"""
    x = 0 
    y = 1 
    posicao = -1 
    while x < len(fragmento) or y == numero :
        if fragmento[x] == letra : 
            y = y + 1  
            posicao = x 
        x = x + 1
    
    return posicao