def posLetra(string,letra, numero):
    '''dada uma string(string), uma letra(letra) e um numero(numero), retorna a posicao ocupada pela (numero)repeticao da letra(letra) na string; str,int,str -> int'''
    indice = 0
    soma = 0
    posicao = 0
    if numero > str.count(string,letra):
        indice = -1
        return indice
    else:
        while indice < len(string):
            if string[indice] == letra:
                soma = soma + 1
            if soma == numero:
                posicao = indice
                return posicao
            indice = indice + 1