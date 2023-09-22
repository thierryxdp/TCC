def primo(numero):
    divisao = []
    for i in range(numero):
        
        if numero%(i+1)==0:
            divisao+= [i]
    if len(divisao)==2:
        return True
    elif len(divisao)>2:
        return False