def pontos_por_time(ce,cs,fv,fe,fs):
    """Função que retorna o resultado de um campeonato entre Cormengo e Flaminthians.
    Use cv: Número de vitórias de Cormengo
    Use ce: Número de empates de Cormengo
    Use cs: Saldo de gols de Cormengo
    Use fv: Número de vitórias de Flaminthians
    Use fe: Número de empates de FLaminthians
    Use fs: Saldo de gols de Flaminthians
    Saída: Int -> Str"""
    cormengo = cv * 3 + ce
    flaminthians = fv * 3 + fe
    if cormengo == flaminthians:
        if cs == fs:
            return 'Empate'
        else:
            if cs > fs:
                return 'Cormengo'
            else:
                return 'Flaminthians'
    else:
        if cormengo > flaminthians:
            return 'Cormengo'
        else:
            return 'Flaminthians'