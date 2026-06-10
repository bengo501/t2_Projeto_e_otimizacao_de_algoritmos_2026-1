"""
Exercício Greedy - Rally pelo deserto de Dakkar
Disciplina: Projeto e Otimização de Algoritmos

Problema: dada uma trilha de comprimento L, uma autonomia diária d e pontos
de parada em distâncias x1 < x2 < ... < xn do início, encontrar o menor
conjunto válido de pontos de parada que permite completar o rally.

Um conjunto de paradas é VÁLIDO se:
  - o primeiro ponto escolhido está a no máximo d do início;
  - a distância entre paradas consecutivas escolhidas é no máximo d;
  - o último ponto escolhido está a no máximo d do final (posição L).

O algoritmo guloso proposto: ao chegar em um ponto de parada, se for possível
alcançar o PRÓXIMO ponto antes de anoitecer, continua dirigindo; caso
contrário, acampa no ponto atual. Isso equivale a, a cada dia, avançar até o
ponto de parada mais distante alcançável a partir do acampamento atual.
"""

from __future__ import annotations


def greedy_paradas(L: float, d: float, pontos: list[float]) -> list[float] | None:
    """Algoritmo guloso: avança ao ponto mais distante alcançável a cada dia.

    Recebe os pontos já ordenados por distância do início e devolve a lista
    de pontos onde o grupo acampa, ou None se a trilha for impossível
    (não ocorre quando o conjunto completo de pontos é válido).

    Complexidade: O(n) - cada ponto é visitado uma única vez.
    """
    pos = 0.0          # posição do acampamento atual (início = 0)
    paradas: list[float] = []
    i = 0
    n = len(pontos)

    # enquanto não for possível chegar ao final em um único dia de viagem
    while L - pos > d:
        # nenhum ponto alcançável hoje -> impossível completar a trilha
        if i >= n or pontos[i] - pos > d:
            return None
        # dirige enquanto o PRÓXIMO ponto ainda é alcançável hoje
        while i + 1 < n and pontos[i + 1] - pos <= d:
            i += 1
        # o próximo não é alcançável (ou não existe): acampa aqui
        paradas.append(pontos[i])
        pos = pontos[i]
        i += 1

    return paradas


def otimo_paradas_dp(L: float, d: float, pontos: list[float]) -> list[float] | None:
    """Solução exata por programação dinâmica, usada para VALIDAR o guloso.

    dp[i] = menor número de paradas para chegar ao ponto i respeitando a
    autonomia d. Devolve uma solução com o número mínimo de paradas.

    Complexidade: O(n^2) - serve apenas como verificador em testes.
    """
    n = len(pontos)
    INF = float("inf")
    # posições: índice 0 = início (posição 0), índices 1..n = pontos
    posicoes = [0.0] + list(pontos)
    dp = [INF] * (n + 1)
    ant = [-1] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if posicoes[i] - posicoes[j] <= d and dp[j] + 1 < dp[i]:
                dp[i] = dp[j] + 1
                ant[i] = j

    # melhor ponto final: de onde se alcança a linha de chegada (posição L)
    melhor, melhor_custo = -1, INF
    if L <= d:
        return []  # chega ao final sem acampar
    for i in range(1, n + 1):
        if L - posicoes[i] <= d and dp[i] < melhor_custo:
            melhor, melhor_custo = i, dp[i]

    if melhor == -1:
        return None

    # reconstrói o caminho
    caminho: list[float] = []
    i = melhor
    while i > 0:
        caminho.append(posicoes[i])
        i = ant[i]
    return caminho[::-1]


def conjunto_valido(L: float, d: float, paradas: list[float]) -> bool:
    """Verifica se um conjunto de paradas é válido conforme o enunciado."""
    anterior = 0.0
    for p in paradas:
        if p - anterior > d:
            return False
        anterior = p
    return L - anterior <= d


if __name__ == "__main__":
    # Exemplo de uso: trilha de 25 km, autonomia de 10 km/dia
    L, d = 25.0, 10.0
    pontos = [4.0, 7.0, 9.0, 12.0, 16.0, 18.0, 21.0, 24.0]

    sol = greedy_paradas(L, d, pontos)
    print(f"Trilha L={L}, autonomia d={d}")
    print(f"Pontos de parada: {pontos}")
    print(f"Paradas escolhidas pelo guloso: {sol} ({len(sol)} paradas)")
    print(f"Conjunto valido? {conjunto_valido(L, d, sol)}")

    otimo = otimo_paradas_dp(L, d, pontos)
    print(f"Solucao otima (DP):            {otimo} ({len(otimo)} paradas)")
