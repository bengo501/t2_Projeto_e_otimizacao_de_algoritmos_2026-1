from __future__ import annotations
#   algoritmo guloso de tempo linear
def greedy_paradas(L: float, d: float, pontos: list[float]) -> list[float] | None:
    pos = 0.0  #   posicao do acampamento atual
    paradas: list[float] = []  #paradas escolhidas
    i = 0  #    indice do ponto sendo analisado
    n = len(pontos)
    while L - pos > d:  #  enquanto nao da para chegar ao final em um dia
        if i >= n or pontos[i] - pos > d:  #  nenhum ponto alcancavel hoje
            return None
        while i + 1 < n and pontos[i + 1] - pos <= d:  # avanca enquanto o proximo ainda e alcancavel
            i += 1
        paradas.append(pontos[i])                      #  acampa no ponto mais distante possivel
        pos = pontos[i]
        i += 1
    return paradas
#  verificador otimo por programacao dinamica em tempo quadratico
def otimo_paradas_dp(L: float, d: float, pontos: list[float]) -> list[float] | None:
    if L <= d:  # chega ao final sem acampar
        return []
    n = len(pontos)
    INF = float("inf")
    posicoes = [0.0] + list(pontos)  #  indice zero e o inicio
    dp = [INF] * (n + 1)                    #    menor numero de paradas para chegar em cada ponto
    ant = [-1] * (n + 1)                    #   ponto anterior para reconstruir o caminho
    dp[0] = 0
    for i in range(1, n + 1):               #    para cada ponto de destino
        for j in range(i):                  #  testa todos os pontos anteriores
            if posicoes[i] - posicoes[j] <= d and dp[j] + 1 < dp[i]:  #transicao valida e mais barata
                dp[i] = dp[j] + 1
                ant[i] = j
    melhor, melhor_custo = -1, INF
    for i in range(1, n + 1):                   # procura o ponto de onde se alcanca o final com menos paradas
        if L - posicoes[i] <= d and dp[i] < melhor_custo:
            melhor, melhor_custo = i, dp[i]
    if melhor == -1:                          # se nenhum ponto alcanca o final
        return None
    caminho: list[float] = []
    i = melhor
    while i > 0:             # volta ate o inicio reconstruindo o caminho
        caminho.append(posicoes[i])
        i = ant[i]
    return caminho[::-1]    #inverte para ficar na ordem da trilha
#   verifica se um conjunto de paradas e viavel em tempo linear
def conjunto_valido(L: float, d: float, paradas: list[float]) -> bool:
    anterior = 0.0
    for p in paradas:
        if p - anterior > d:  #trecho maior que a autonomia
            return False
        anterior = p
    return L - anterior <= d  #o ultimo trecho tambem precisa caber em um dia
#  exemplo de uso para testes e validacao do algoritmo
if __name__ == "__main__":
    L, d = 25.0, 10.0  #    trilha de 25 km e autonomia de 10 km por dia
    # pontos de parada disponiveis
    pontos = [4.0, 7.0, 9.0, 12.0, 16.0, 18.0, 21.0, 24.0]
    sol = greedy_paradas(L, d, pontos)
    otimo = otimo_paradas_dp(L, d, pontos)
    print(f"L={L} d={d} pontos={pontos}")
    print(f"guloso={sol} ({len(sol)} paradas) valido={conjunto_valido(L, d, sol)}")
    print(f"otimo ={otimo} ({len(otimo)} paradas)")
