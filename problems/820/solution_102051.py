def posLetra(string,letra,num):
    '''Função que retorna a posição da ocorrencia "num" de uma letra na frase
    string, string, int -> int'''
    i = 0
    lista = []
    while i<len(string):
        if string[i] == letra:
            lista.append(i)
            #Adiciona na lista um apêndice quando i = posiçãio da ocorrência da letra na string
        i = i + 1
        
    
    if len(lista) >= num:
        return lista[num-1]
    if len(lista)<num:
        return -1