def lingua_p(palavra):
    traducao=''
    for i in palavra:
        if i in 'aeiouAEIOUáéíóúàãõêôÁÉÍÓÚÃÕÀÊÔ':
            traducao+=i+'p'+i
        else:
            traducao+=i
    return traducao