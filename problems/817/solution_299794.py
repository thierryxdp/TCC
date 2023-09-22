def acima_da_media(lista):
    """Função que, dada uma lista com as notas dos alunos 
    de uma turma, retorna uma lista ordenada com as notas que
    estao acima da média 
    list -> list"""
    s = sum(lista)
    d = len(lista)
    numero=s/d
    copia=list.copy(lista)
    a=maiores(copia,numero)
    list.pop(a,0)
    if numero in a:
        b=list.index(a,numero)
        list.pop(a,b)
    return a