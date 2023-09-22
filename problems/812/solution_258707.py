def retira_pontuacao(frase):
    """Retorna uma frase igual a de entrada, mas como a sua pontuação substituída por espaço.
    string --> string"""
    
    frase_nova = str.replace(frase,'.' , ' ') and str.replace(frase,'...' , ' ') and str.replace(frase,'?' , ' ') and str.replace(frase,'!' , ' ') and str.replace(frase,'-', ' ') and str.replace(frase,',' , ' ') and str.replace(frase,':' , ' ') and str.replace(frase,';', ' ')  
    
    return frase_nova