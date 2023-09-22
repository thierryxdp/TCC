def conta_frases(T):
    """Funcao que, dado um texto T, conta o numero de frases
    que aparecem neste texto. Cada frase no texto é terminada
    com um ponto final, um ponto de exclamacao, um ponto de 
    interrogacao ou tres pontos em sequencia(reticencias).
    Pontos de exclamacao ou de interrogacao nao aparecem
    repetidos em sequencia no texto e esses simbolos so 
    aparecem no texto terminando uma frase. No exemplo a 
    seguir, sao contadas 4 frases:"Preciso tirar um cochilo.
    Meu Deus! Que horas sao? Vou perder a minha aula...";
    str->int"""
    return (str.count(T,".")+str.count(T,"!")
            +str.count(T,"?")+str.count(T,"..."))