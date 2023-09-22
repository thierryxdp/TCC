def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase trocando todos os caracteres de pontuacao por espaço em branco"""
    """entrada: str
    saida: str"""
    
    a = str.split(frase,"-")
    b = str.split(frase,",")
    c = str.split(frase,":")
    d = str.split(frase,";")
    e = str.split(frase,".")
    f = str.split(frase,"!")
    g = str.split(frase,"?")
    
    return str.join(" ",a)+str.join(" ",b)+str.join(" ",c)+str.join(" ",d)+str.join(" ",e)+str.join(" ",f)+str.join(" ",g)