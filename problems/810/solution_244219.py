def retira_pontuacao(x):
    """função que vai receber uma frase e depois vai 
    retornar a frase revertirda: str->str"""
    x=str.replace(x,",","")
    f=str.replace(x,".","")
    f=str.replace(x,"-","")
    f=str.replace(x,"?","")
    f=str.replace(x,":","")
    f=str.replace(x,"!","")
    f=str.replace(x,"...","")
    f=str.replace(x,";","")
    return x
def inverte(x):
    x=str.replace(x,"-", " ")
    y=str.split(x)
    z=str.lower(' '.join(list(reversed(y))))
    return retira_pontuacao(z)