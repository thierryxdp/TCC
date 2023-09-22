def lingua_p(palavra):
    'função que traduz uma palavra do portugues para a lingua do p, sendo a lingua do p a mesma palavra que em portugues com p sempre antes de cada vogal '
    for i in palavra:
        if i in 'aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛàèìòùÀÈÌÒÙ':
            palavra=str.replace(palavra,i,'p'+i)
    return palavra