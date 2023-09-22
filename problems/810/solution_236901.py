def inverte(frase):
    """Função na qual dada uma frase retorna a mesma frase de tras para frente e com todas as letras minusculas"""
    nova_frase = frase.lower()
    nova_frase_2 = retira_pontuacao(nova_frase)
    l = nova_frase_2.split(' ')
    l.reverse()
    return ' '.join(l)