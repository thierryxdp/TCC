def pontos_por_time(jogo_da_ida,jogo_da_volta):
        t1 = jogo_da_ida[0]
        t2 = jogo_da_ida[1]
        p_t1 = jogo_da_ida[2][0] + jogo_da_volta [2][1]
        p_t2 = jogo_da_ida[2][1] + jogo_da_volta [2][0]
        return {t1:p_t1, t2:p_t2}