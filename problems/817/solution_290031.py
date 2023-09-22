def acima_da_media (notas):
    '''Função que recebe uma lista com as notas dos alunos da turma
    e retorna uma lista ordenada com as notas que ficaram
    acima da média
    float->list'''
    media=sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    resultado=notas[:list.index(notas,media):-1]
    if media in resultado:
        list.remove(resultado,media)
        list.sort(resultado)
        return resultado
    else:
        return list[min(resultado),max(resultado)]