def retira_pontuacao(frase):
    """ funcao que ,dada uma frase,retorna uma nova onde todos os caracteres de pontuaçao são substituidos por espaço,str,str ->str"""
    
    return str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),'?',' '),',',' '),'-',' ')