def lingua_p(palavra):
    traducao=''
    for i in palavra:
        if i in 'AEIOUaeiouáéíóúÁÉÍÓÚ':
            traducao=traducao+i+'p'+i
        else:
            traducao=traducao+i
    return traducao