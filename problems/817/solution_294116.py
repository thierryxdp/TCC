#1.Definir a media da turma
#2.Organizar as notas
#3.Localizar a primeira nota que atingiu a media da turma
#4.Fatiar da média(exclusive) adiante
#5.Retornar lista

def acima_da_media(notas:list)->list:
    """funcao que ordena as notas de uma turma
    e separa as notas acima da media da turma"""
    
    media=sum(notas)/len(notas)
    notas.append(media)
    list.sort(notas)
    local=list.index(notas,media)
    
    if notas[local]==notas[local+1]:
        return notas[local+2:]
    else:
        return notas[local+1:]