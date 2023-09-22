def lingua_p(palavra):
    resposta=''
    for i in palavra:
        if i in 'aiouáéíóúÁÉÍÓÚAEIOU':
            resposta= resposta+'p'+i
        else:
            resposta= resposta+i
    return resposta