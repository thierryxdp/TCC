def posLetra(frase,letra,num):
    """Recebe uma frase, uma letra e um número e retorna um número que equivale
    a ocorrência 'num' da letra 'letra' na frase dada. Caso não haja ocorrências
    suficientes retorna -1.
    Assinatura: str,str,int -> int"""
    o=0
    for i in range(len(frase)):
        if frase[i] == letra:
            o+=1
        if o == num:
            return i
        else:
            return -1