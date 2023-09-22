def acima_da_media(notas):
    '''função que retorna uma lista ordenada com as notas dos alunos
    que ficaram acima da média.
    lista -> lista'''
    
    media = sum(notas)/len(notas)
    maiores = []
    
    for i in range(len(notas)):
        if notas[i] > media:
            maiores.append(notas[i])
    notas = maiores
            
    return notas