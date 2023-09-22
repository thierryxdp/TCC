def acima_da_media (lista):
    """dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média.
    
    entrada-> list 
    return-> list"""
    
    quant_alunos=len (lista)
    somatdnotas=sum (lista)
    media= somatdnotas/quant_alunos
    
    return media