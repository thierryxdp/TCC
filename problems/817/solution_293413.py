#Entrada:lista com notas 
#Analisa as notas acima da média e retorna uma lista ordenada com elas
def acima_da_media(notas:list)->list:
    """A função recebe a lista de notas dos alunos
    de uma turma e retorna a lista ordenada das 
    notas"""
    media=sum(notas)/len(notas)
    notas.append(media)
    list.sort(notas)
    indice=list.index(notas,media)
    del notas[indice]
    return notas[indice+1:]