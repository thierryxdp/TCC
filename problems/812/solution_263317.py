def retira_pontuacao(frase):
    '''
    dada uma frase como parametro, retorna os caracteres de pontuação substituidos por espaços
    str--->str
    '''

    
    texto1= str.replace(frase,"-"," ")
    texto2= str.replace(texto1,":"," ")
    texto3= str.replace(texto2,"."," ")
    texto4= str.replace (texto3,","," ")
    return texto4