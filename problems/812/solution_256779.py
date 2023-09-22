def retira_pontuacao(frase):
    '''funçao que dada uma frase retira todos os pontos e poe espaço'''
    att1 = frase.replace("."," ")
    att2 = att1.replace("-"," ")
    att3 = att2.replace(","," ")
    att4 = att3.replace(":"," ")
    att5 = att4.replace(";"," ")
    return att5