def acima_da_media(notas):
    """funcao que retorna uma lista em ordem com as notas dos alunos que ficaram acima da media"""
    soma=sum(notas)
    num=len(notas)
    media=int((soma/num)+1)
    list.append(notas,media)
    list.sort(notas)
    ordemMedia=notas.index(media)
    return notas[ordemMedia+1:]