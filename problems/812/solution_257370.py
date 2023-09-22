def retira_pontuacao(frase):
    '''dada uma frase a função substitui a pontuação por espaço'''

    x=frase.replace("!"," ").replace("?"," ").replace("..."," ").replace("."," ").replace("-"," ").replace(":"," ").replace(";"," ").replace(","," ")

    return x