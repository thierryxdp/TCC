def posLetra(string,letra,num):
    """ recebe uma string, uma letra e um numero e retorna a posição da letra na
    string na ocorrencia desejada(num). e caso não exista, a funçao retorna -1;
    str,str,int->int"""
    if list(string).count(letra)>=num:
        return str.find(str.replace(string,letra,"@",num-1),letra,0,-1):
    else:
        return -1