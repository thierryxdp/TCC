def melhor_volta(M):
    """Função que retorna o piloto, o tempo e o número da melhor volta. A
    entrada da função é uma matriz cujas linhas correspondem ao piloto e as
    colunas às voltas e os elementos representam justamente o tempo de um
    piloto i na volta j
    list -> tuple(int, float, int)"""
    m_individuais=[]
    q_voltas=[]
    for i in range(len(M)):
        m_volta_p=min(M[i])
        volta_n=list.index(M[i],min(M[i]))
        list.append(m_individuais,m_volta_p)
        list.append(q_voltas,volta_n)
    m_volta=min(m_individuais)
    m_piloto=list.index(m_individuais,m_volta)+1
    q_volta=q_voltas[m_piloto-1]+1
    return m_piloto,m_volta,q_volta