def retira_pontuacao(frase):
    """Funcao que, dada uma frase, retorna a frase com todos os caracteres de pontuacao substituidos por espaco;
    Entrada: str
    Saida: str"""

    editada = str.replace(frase,'.',' ')
    editada = str.replace(editada,',',' ')
    editada = str.replace(editada,'-',' ')
    editada = str.replace(editada,':',' ')
    editada = str.replace(editada,';',' ')
    editada = str.replace(editada,'!',' ')
    editada = str.replace(editada,'?',' ')


    return editada

def inverte(frase):
    """Funcao que recebe uma frase e retorna outra com as mesmas palavras mas na ordem inversa, sem letras maiusculas e sem pontuacao;
    Entrada: str
    Saida: str"""
    
    frase = str.lower(frase)
    editada = retira_pontuacao(frase)
    lista = str.split(editada)
    lista = lista[::-1]
    lista = str.join(' ',lista)

    return lista