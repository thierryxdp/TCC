def acima_da_media (notas):
    '''dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media
       : list -> list 
    '''
    media = sum(notas)/len(notas)
    Mmedia = maiores (notas, media)
    
    return Mmedia