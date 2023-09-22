def posletra(frase,letra,numero):
    "A função recebe uma frase, uma letra e um numero e retorna a ocorrencia desejada da letrae caso exista menos ocorrências retorna -1. assinatura: str, str, int --> int"""
    o = 0
    for i in range (len(frase)):
        if o == numero: 
            return i-1 
        if frase [i] == letra: 
            o += 1 
    if o < numero:
            return -1