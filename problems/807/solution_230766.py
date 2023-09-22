def conta_frases(txt):
    """Recebe uma string contendo um texto como parâmetro e retorna o número de frases contidas no texto. Cada frase no texto é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou três pontos em sequência (reticências). Pontos de exclamção ou de interrogação não podem aparecer repetidos em sequência e só podem aparecer terminando uma frase;
    assinatura: string --> int
    Casos de teste:
    conta_frases('Meu nome é Luciano. Tenho 20 anos! Faço EN na UFRJ. E você?') == 4
    conta_frases('Semana que vem tem duas provas! E dois trabalhos. E na semana seguinte? Mais duas provas. E mais trabalhos...') == 5
    conta_frases('Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder minha aula...') == 4
    """
    n = 0
    txt = txt.split()
    for e in txt:
        if e[-1] == '.' or e[-1] == '!' or e[-1] == '?':
            n += 1
    return n