def posLetra(frase, letra, num):
    """ Funçao que retorna em que posição da string(frase)
    a letra que aparece na vez de numero(num) está"""
    if str.count(frase,letra) < num:
        return -1
    else: 
        lista =[]
        i = 0
        while i < len(frase):
            list.extend(lista,frase[i])
            i = i+1   
        a = 0
        while a < (num - 1):
            posicao = list.index(lista,letra)
            lista[posicao] = " "
            a = a+1
            return lista.index(lista,letra)