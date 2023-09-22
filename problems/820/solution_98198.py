def posLetra(fragmento,letra,numero) : 
    """Retorna em que posição da string a ocorrência dela 
    está localizada, exemplo : ("dinheiro","i",2) onde está o
    segundo "i" na palavra "dinheiro";
    str, str, int -> int"""
    x = 0 
    posicao = 0 
    while x < len(fragmento) :
        if fragmento[x] == letra : 
            posicao = x 
        x = x + 1
        else :
            posicao = -1
    
    return posicao