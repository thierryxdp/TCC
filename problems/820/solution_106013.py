def posLetra(string="",letra="", num=0):
    '''funcao que recebe uma string, uma letra e um numero que indica a
    ocorrência desejada da letra e retorna a posição'''
    if (string.count(letra)>=num):
        lista = list(string)
        for i in range(num-1)
        numb = int(lista.index(letra))
        lista[numb] = " "
        string="".join(lista)
        return string.index(letra)
    
    return -1