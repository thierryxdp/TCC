def posLetra( nome, letra, n):
    ''' retorna a posição em que está a ocorrência da string; 
    entrada -> string, letra, ocorrencia; str, str, int -> int'''
    lst= []
    for pos,char in enumerate(nome):
        if(char == letra):
            lst.append(pos)
    if n > len(lst):
      	return -1
    else:
      	return lst[n-1]