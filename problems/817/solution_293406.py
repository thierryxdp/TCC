#Entrada:lista com notas 
#Analisa as notas acima da média e retorna uma lista ordenada com elas
def acima_da_media(notas:list)->list:
    """A função recebe a lista de notas dos alunos
    de uma turma e retorna a lista ordenada das notas
    acima da média"""
    media=sum(notas)/len(notas)
    notas.append(int(media))
    list.sort(notas)
    indice=list.index(notas,int(media))
    return notas[indice+1:]