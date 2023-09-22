def posLetra (frase,letra,n):
    '''funcao que dado uma string,uma letra
    e um numero 'n' retorna a posicao 'n'
    da letra na string; str,str,int -> int'''
    
    if str.count(frase,letra) < n:
        return -1
    
    else:
        i = 0
        while i < len(frase):
            if frase[i] != letra:
                i = i + 1
        return i