def posLetra(string,letra,num):
    '''funcao que verifica e retorna a posição de uma determinada letra em um string;
    str, str, int -> int'''
    pos_letra = 0
    while pos_letra < len(string):
        if num > len(str.find(string,letra)):
            return -1
        str.find(string,letra,num)
    return pos_letra