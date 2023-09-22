def posLetra(f,l,n):
    '''Essa função ao receber como valor de entrada uma string, uma letra e um número que indica a ocorrência desejada da letra, ela retornar em que posição da string aquela ocorrência da letra está.'''
    '''str,str,int -> int'''
    
    pos = 0
    rep = 0
    
    while pos < len(f):
          
          if f[pos] == l:
                rep = rep + 1
                
                if rep == n:
                    return pos 
         
          pos = pos + 1
    return -1