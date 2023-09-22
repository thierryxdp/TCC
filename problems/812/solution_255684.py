def retira_pontuacao(frase):
    """ESSA FUNÇÃO DADA UMA FRASE RETORNA A MESMA FRASE ONDE TODOS OS CARACTERES, SÃO SUBSTITUIDOS POR UM ESPAÇO"""
    caracteres = ('\\','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'')
    frase = str.split(frase, caracteres)
    frase = str.joint(" ",frase)
    return frase