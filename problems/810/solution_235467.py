def retira_pontuacao(frase):
    """Função que retira todos os caracteres de pontuação da frase fornecida como entrada e os substitui por espaços."""
    """str-->str"""
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    return frase

def inverte(frase):
    """Função que, dada uma frase, retorna uma outra frase que contenha as mesmas palavras de entrada, porém na ordem inversa, sem letras maiúsculas e sem a pontuação."""
    """str-->str"""
    a=retira_pontuacao(frase)
    a=str.split(str.lower(a))
    a= a[len(a)+1::-1]
    
    return ' '.join(a)