def acima_da_media(lista):
    """dada uma lista com as notas de uma turma retorna 
    uma lista das notas acima da media"""
   
    a=sum(lista)
    
    b=(len(lista))
  
    x=a/b
    
    lista.append(x)
    
    lista.sort()
    
    z=lista.index(x)
   
       return lista[z+1:]