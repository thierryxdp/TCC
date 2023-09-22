def lingua_p(palavra):
    ''' funcao recebe uma palavra e a cada vogal dessa palavra
    e acrescentado um p e a vogal orignal, str-->str'''
    nw=''
    for c in palavra:
        if c in 'AEIOUaeiou':
            nw+= str.replace(c,c+p+c)
        else:
            nw= c