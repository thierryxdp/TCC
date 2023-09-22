def conta_frase(string):
    """Essa função retorna a quantidade de frases presentes na string 
    informada. Como entrada temos uma string e como saída temos o número
    de frases informadas dentro da mesma string;
    str-> int"""
    frase1=str.replace(string,"."," ")
    frase2=str.replace(frase1,"!"," ")
    frase3=str.replace(frase2,"?"," ")
    frase4=str.replace(frase3,"..."," ")
    frase=str.split(frase4," ")
    numerodefrase=len(frase)