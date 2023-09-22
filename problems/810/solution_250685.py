def retira_pontuacao(frase):
    """Recebe como parâmetro uma string contendo uma frase e retorna a frase com todos os caracteres de pontuação substituídos por espaço. São considerados caracteres de pontuação: travessão, vírgula, dois pontos, ponto e vírgula, ponto final, ponto de exclamação, ponto de interrogação e reticências;
	assinatura: string --> string
    Casos de teste:
    retira_pontuacao('Meu nome é Luciano. Tenho 20 anos! Faço EN na UFRJ. E você?') == 'Meu nome é Luciano  Tenho 20 anos  Faço EN na UFRJ  E você '
    retira_pontuacao('Semana que vem tem duas provas! E dois trabalhos. E na semana seguinte? Mais duas provas. E mais trabalhos...') == 'Semana que vem tem duas provas  E dois trabalhos  E na semana seguinte  Mais duas provas  E mais trabalhos   '
    retira_pontuacao('Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder minha aula...') == 'Preciso tirar um cochilo  Meu Deus  Que horas são  Vou perder minha aula   '
    """
    frase = frase.split()
    for i, e in enumerate(frase):
        if e[-1] == '.':
            frase[i] = e.replace('.', ' ')
        elif e[-1] == '!':
            frase[i] = e.replace('!', ' ')
        elif e[-1] == '?':
            frase[i] = e.replace('?', ' ')

    for i, e in enumerate(frase):
        if '-' in e:
            frase[i] = e.replace('-', ' ')
        elif ',' in e:
            frase[i] = e.replace(',', ' ')
        elif ':' in e:
            frase[i] = e.replace(':', ' ')
        elif ';' in e:
            frase[i] = e.replace(';', ' ')
            
    return ' '.join(frase)

def inverte(frase):
    retira_pontuacao(frase)
    frase = frase.split()
    lista1 = []
    for i, p in enumerate(frase):
        i = -(i +1)
        lista1.append(i)
    lista2 = []
    for e in lista1:
        lista2.append(frase[e])
    return ' '.join(frase)