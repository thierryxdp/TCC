def lingua_p(palavra):
    palavraP=str()
    'função que traduz uma palavra do portugues para a lingua do p, sendo a lingua do p a mesma palavra que em portugues com p sempre antes de cada vogal '
    for i in palavra:
        if i in 'aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛàèìòùÀÈÌÒÙ':
            palavraP= palavraP +i+'p'
        else:
            palavraP= palavraP+i
    return palavraP