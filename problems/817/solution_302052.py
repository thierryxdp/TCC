def acima_da_media(listanotas):
    '''Função que dada uma lista com as notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas que ficaram acima da média
    '''
    tamanho=len(listanotas)
    soma=sum(listanotas)
    media=(soma)/(tamanho)
    bigger=media+0.5
    
    return maiores(listanotas,bigger)