def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase trocando todos os caracteres de pontuacao por espaço em branco"""
    """entrada: str
    saida: str"""
    
    1 = str.split(frase,"-")
    2 = str.split(frase,",")
    3 = str.split(frase,":")
    4 = str.split(frase,";")
    5 = str.split(frase,".")
    
    return str.join(" ",[1,2,3,4,5])