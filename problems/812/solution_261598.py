def retira_pontuacao (frase):
    '''dada uma frase, retorna a frase com os caracteres de pontuaçao substituidos por espaço
       : str -> str
    '''
   # x = '-',',',':',';','.'
    #if x in frase:
       # nova_frase = frase.replace(x,'/')
        nova_frase = frase.remove('-',',',':',';','.')
        return nova_frase