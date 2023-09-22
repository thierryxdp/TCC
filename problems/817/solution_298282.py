def acima_da_media(lista):
    """dada uma lista com as notas dos alunas de sua turma, retorna uma lista ordenada com as notas que ficaram acima de média. Lista--> Lista"""
  
    
    b=int(len(lista))
    c=sum(lista)
    m=c/b
    lista.append(m)
    list.sort(lista)
    a=int(lista.index(m))+1
    d=lista.count(m)
  
    f=int(lista.count(m))
    e=int(a+f-1)
    if b==1:
        return []
    if f>1:
        return lista[e:]
    
    elif a!=m:
        return lista[a:]