def conta_frases(frase):
    """Função que, dada um texto, retorna sua quantidade
    str-> int """
    f1=["Preciso tirar um cochilo."]
    f2=["Meu Deus!"]
    f3=["Que horas são?"]
    f4=["Vou perder a aula..."] 
    frase=[f1,f2,f3,f4] 
     
    return len(frase.split())