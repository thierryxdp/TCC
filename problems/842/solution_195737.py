def pontos_por_time (ida = [], volta = []):
    """calcula quantos pontos o time tem no final do campeonato dado os placares."""
    ida = [ida[0], ida[1], ida[3]]
    volta = [volta[0], volta[1], volta[2]]
    ida[3] = [ida[0], ida[1]]
    volta[3] = [volta[0], volta[1]]
    if ida[3[0]] == ida[3[1]]:
        return True