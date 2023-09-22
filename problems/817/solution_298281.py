def acima_da_media(notas_dos_alunos):
    '''dado apenas as notas dos alunos em formato de lista
    temos como retornar uma lista na qual inclua apenas
    as notas maiores que a media dos alunos e organizada 
    de maneira crescente'''
    notaMedia=sum(notas_dos_alunos)/len(notas_dos_alunos)
    listaNumerosMaiorIgualMedia=maiores(notas_dos_alunos,notaMedia)
    numerosIguaisAMedia=listaNumerosMaiorIgualMedia.count(notaMedia)
    listaComApenasAsNotasAcimaDaMedia=listaNumerosMaiorIgualMedia[numerosIguaisAMedia:]
    return listaComApenasAsNotasAcimaDaMedia