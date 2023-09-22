def acima_da_media(notas):
    '''Função que dada uma lista de notas de alunos de uma turma retorna
uma lista ordenada com notas que ficaram acima da média.
    lista -> lista'''
    
    Media = sum(notas)/len(notas)
    
    if Media not in notas:
        notas.append(Media)
        
    numeros.sort()
    
    return notas[notas.index(Media)+notas.count(Media):]