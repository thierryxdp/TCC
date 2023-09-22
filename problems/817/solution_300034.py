def acima_da_media(lista_de_notas, n):
    """Funçao que faz a media das notas dos alunos"""
    "list-->list"
     
    n=int(n)
    
    
    list.sort(lista_de_notas)

    if n > max(lista_de_notas):
        return []
    elif n < max(lista_de_notas):
           
        return 9