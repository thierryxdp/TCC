def lingua_p(palavra):
    traducao=''
    for i in palavra:
        if i in 'aeiouAEIOU':
            traducao+=i+'p'+i
        else:
            traducao+=i
    return traducao