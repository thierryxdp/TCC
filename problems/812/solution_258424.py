def retira_pontuacao(texto):
    """Retorna o texto onde todos os caracteres de pontuação tenham sido substituídos por espaço"""
    """str -> str"""
    /
    ,
    ":"
    ;
    !
    ?
    ...
    .
    
    
    return str.replace(texto, "/" or "," or ":" or ";" or "!" or "?" or "..." or ".", " ")