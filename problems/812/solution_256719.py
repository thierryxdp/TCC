def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase trocando todos os caracteres de pontuacao por espaço em branco"""
    """entrada: str
    saida: str"""
    
    a = str.split(frase,"-")
    b = str.split(frase,",")
    c = str.split(frase,":")
    d = str.split(frase,";")
    e = str.split(frase,".")
    
    return str.join(" ",abcde)