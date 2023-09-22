def retira_pontuacao(frase):
    '''dada uma frase, retorna uma frase onde todos os caracteres de pontuaçao foram
substituidos por espaço. str -> str.'''
	nova_frase = ""
    nova_frase = frase
    nova_frase = str.replace(nova_frase,"!"," ")
    nova_frase = str.replace(nova_frase,"-"," ")
    nova_frase = str.replace(nova_frase,","," ")
    nova_frase = str.replace(nova_frase,"."," ")
    nova_frase = str.replace(nova_frase,";"," ")
    nova_frase = str.replace(nova_frase,":"," ")
    nova_frase = str.replace(nova_frase,"?"," ")
    return nova_frase