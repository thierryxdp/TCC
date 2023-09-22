def acima_da_media(lista):
    """Dá uma lista ordenada com alunos que ficaram acima da média
    	list -> list
        Parameters:
        lista: Lista com notas dos alunos
        
        Returns:
        Lista ordenada com alunos que ficaram acima da média
     """
    
   a=sum(lista)/len(lista)
   list.append(lista,a)
   list.sort(lista)
   p=list.index(lista,a)
   n=list.count(lista,a)

   return a, lista[p+1:]