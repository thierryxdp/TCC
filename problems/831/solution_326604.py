def lingua_p(palavra):
    ''' determinando todas as variaões de vogal
    e acrescentando o p antes e depois'''
    resposta=''
    for i in palavra:
        if i in 'aeiouáéíóúÁÉÍÓÚAEIOU':
            resposta= resposta+ i +'p'+i
        else:
            resposta= resposta+i
    return resposta