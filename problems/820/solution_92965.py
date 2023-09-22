def posLetra(string, letra, n):
    '''recebe como entrada uma string, uma letra, e um número que indica
    a ocorrencia desejada da letra. Retorna em que posição da string a 
    ocorrência da letra está. Caso exista menos ocorrências da letra do 
    que a ocorrência pedida, a função retorna -1'''
    ocorrencias_letra =str.count(string, letra)
    if ocorrencias_letra <n:
        return -1
    i =0
    count =0
    while i <len(string) and count <n:
        if string[i] ==letra:
            count =count +1
            
        i =i+1
    return i-1