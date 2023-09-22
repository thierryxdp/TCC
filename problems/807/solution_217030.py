def conta_frases(text):
    """ Função que calcula o número de frases em um texto 
    Entrada:String 
    Saída: Int"""
    v1 = str.replace(text,'..'','.')
    pontoF  = len(str.split(v1,'.'))-1
    pontE = len(str.split(text,'!'))-1
    pontoI = len(str.split(text,'?'))-1
    somo = pontoF + pontoE + pontoI