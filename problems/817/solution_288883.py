def acima_da_media(lista_notas):
    ''' Dada uma lista com as notas dos alunos, a funcao retorna uma outra 
    lista com as notas que ficaram acima da media de notas; 
    
    list -> list '''
    
    # 1. fazer a média entre as notas
    media = sum(lista_notas)/len(lista_notas)
    
    # 2. colocar essa media na lista original
    list.append(lista_notas,media)
    
    # 3. organizar (com o .sort) na ordem decrescente
    list.sort(lista_notas,reverse = True)
    
    # 4. descobrir o índice da média
    indice_media = list.index(lista_notas,media)
    
    # 5. pegar todos os numeros do indice 0 até o anterior à média
    maiores_notas = lista_notas[0:indice_media]
    
    # 6. arrumar a lista nova com o sort na ordem crescente
    list.sort(maiores_notas)
    
    return maiores_notas