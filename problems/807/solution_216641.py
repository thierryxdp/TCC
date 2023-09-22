def conta_frases(x):
    """ Função que calcula o número de frases em um texto 
    Entrada:String 
    Saída: Int"""
    resposta = ()
    ponto = (len(str.split(x,'.')))-1
    exclamacao = (len(str.split(x,'!')))-1
    interrogacao= (len(str.split(x,'?')))-1
    reticencias = (len(str.split(x,'...')))-1
    return str.replace(ponto+exclamacao+interrogacao+reticencias)