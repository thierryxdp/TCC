def lingua_p (palavra):
    palavrafinal = ''
    for i in palavra:
        if i in 'aeiouAEIOUáéíóúâêîôû':
            palavrafinal = palavrafinal + i +  'p' + i
        elif i not in 'aeiouAEIOUáéíóúâêîôû':
            palavrafinal = palavrafinal + i
    return palavrafinal