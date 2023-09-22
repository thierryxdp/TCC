def inverte(frase):
    semtravessao=str.replace(frase, "-", " ",-1)
    semvirgula=str.replace(semtravessao,","," ",-1)
    semdoispontos=str.replace(semvirgula,":", " ",-1)
    sempontoevirgula=str.replace(semdoispontos,";"," ",-1)
    sempontofinal=str.replace(sempontoevirgula,"."," ",-1)
    seminterrog=str.replace(sempontofinal,"?"," ",-1)
    semexclam=str.replace(seminterrog,"!"," ",-1)
    minusculo=str.lower(semexclam)
    separado=str.split(minusculo,' ')
    reverte= separado.reverse()
    junto=str.join(" ",reverte)
    return junto