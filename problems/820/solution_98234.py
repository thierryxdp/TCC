def posLetra(fragmento,letra,numero) : 
    """Retorna em que posição da string a ocorrência dela 
    está localizada, exemplo : ("dinheiro","i",2) onde está 
    o segundo "i" na palavra "dinheiro";
    str, str, int -> int"""
    x = 0 
    posicao = [] 
    while x < len(fragmento) :
        if fragmento[x] == letra : 
            list.append(posicao,x)  
        x = x + 1
    
    if len(posicao) >= numero :
        return posicao[numero-1]
    elif len(posicao) < numero : 
        return -1