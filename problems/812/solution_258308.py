def retira_pontuacao(x):
    '''função dada uma frase, retorne a mesma sem os caracteres de pontuação e substitua por espaços
   str -> tupla'''
    y= x.replace("."," ")
    z= y.replace("!"," ")
    w= z.replace(","," ")
    g= w.replace("-"," ")
    h= g.replace("?"," ")
    return h