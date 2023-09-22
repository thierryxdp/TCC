def posLetra(s,letra,numero):
    '''Função que retorna em que posição da string aquela ocorrencia da letra está, dada uma string
    str,str,int -> int'''
	i = 0
    x = ''
    while i<=len(s):
        if letra in s:
            if numero>str.count(s,letra):
                return -1
            else:
                return str.find(s,letra,numero-1)
   		i = i + 1
    return x