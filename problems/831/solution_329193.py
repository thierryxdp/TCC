def lingua_p (palavra):
    palavrafinal = ''
    for i in palavra:
        if i in 'aeiouAEIOU':
            palavrafinal = palavrafinal + i +  'p' + i
        elif i not in 'aeiouAEIOU':
            palavrafinal = palavrafinal + i
    return palavrafinal