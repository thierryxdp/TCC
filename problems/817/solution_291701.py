def acima_da_media(lista):
    """Com base na funcao do exercicio 4, calcula quais alunos ficaram
acima da media.
list-->list"""
    
    n= sum(lista)//len(lista) +1 
    
   
    return maiores(lista,n)