def conta_frases(texto):
    '''Função que conta o número de frases que aparece em um texto
    str -> str'''
    
    frase_sem_ret = texto.split('...')
    frase_sem_ret = ' '.join(frase_sem_ret)
    print(frase_sem_ret)

    frase_sem_exc = frase_sem_ret.split('!')
    frase_sem_exc = ' '.join(frase_sem_exc)
    print(frase_sem_exc)

    frase_sem_pont = frase_sem_exc.split('.')
    frase_sem_pont = ' '.join(frase_sem_pont)
    print(frase_sem_pont)

    frase_sem_interr = frase_sem_pont.split('?')
    frase_sem_interr = ' '.join(frase_sem_interr)
    print(frase_sem_interr)

    lista = frase_sem_interr.split('  ')

    quantidade = len(lista)
                    
    return quantidade