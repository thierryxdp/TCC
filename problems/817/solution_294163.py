def acima_da_media(L):
    """Funcao que dada uma lista L com as notas dos alunos
    de uma turma, retorna uma lista ordenada com as notas
    que ficaram acima da media;
    lista->lista"""
    
    Media=(sum(L)/len(L))
    
    list.append(L,Media)
    list.sort(L)
    Valor1=list.index(L,Media)
    Valor2=list.count(L,Media)
    Valor3=(Valor1+Valor2-1)
    
    return L[(Valor3+1):]