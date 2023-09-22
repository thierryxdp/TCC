def inverte(frase):
    """Recebe como parâmetro uma string contendo uma frase e retorna uma string contendo uma outra frase que contém as mesmas palvras da frase de entrada na ordem inversa, sem letras maiúsculas e sem a pontuação;
    assinatura: string --> string
    Casos de teste:
    inverte('Meu nome é Luciano. Tenho 20 anos! Faço EN na UFRJ. E você?') == 'você e ufrj na en faço anos 20 tenho luciano é nome meu'
    inverte('Semana que vem tem duas provas! E dois trabalhos. E na semana seguinte? Mais duas provas. E mais trabalhos...') == 'trabalhos mais e provas duas mais seguinte semana na e trabalhos dois e provas duas tem vem que semana'
    inverte('Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder minha aula...') == 'aula    minha perder vou são  horas que deus  meu cochilo  um tirar preciso'
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
            
    frase = ' '.join(frase)
    frase = frase.split()
    
    lista1 = []
    for i, ch in enumerate(frase):
        i = -(i +1)
        lista1.append(i)
        
    lista2 = []
    for e in lista1:
        frase[e] = frase[e].strip()
        lista2.append((frase[e]).lower())
    
    return ' '.join(lista2)