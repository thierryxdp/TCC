def retira_pontuacao(frase):
    '''...'''
    palavra = str.replace(frase, ',',' ')
    palavra = str.replace(frase, '.',' ')
    
    return str.split(palavra)