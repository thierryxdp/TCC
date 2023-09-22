def acima_da_media(lista):
    """Dá uma lista ordenada com alunos que ficaram acima da média
    	list -> list
        Parameters:
        lista: Lista com notas dos alunos
        
        Returns:
        Lista ordenada com alunos que ficaram acima da média
     """
    
   a=sum(notas)/len(notas)
   list.append(notas,a)
   list.sort(notas)
   p=list.index(notas,a)
   n=list.count(notas,a)

   return a, notas[p+1:]