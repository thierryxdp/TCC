def lingua_p(palavra):
    '''
    função que recebe como parametro uma palavra e retorna tal palavra traduzida 
    para a lingua do P. A lingua do P consiste em inserir um "P" após cada vogal
    da palavra original, sem esquecer de acrescentar depois a vogal original.
    A função ignora a diferença entre minusculo e maiusculo, retornado sempre a 
    palavra toda em minusculo
    str->str
    '''
    x=str.lower(palavra)
    i=0
    palavraP=''
    while i<len(x):
        if x[i] not in "aeiouáéú":
            palavraP=palavraP+x[i]
        
        else:
            palavraP=palavraP+x[i]+"p"+x[i]
        i=i+1
    return palavraP