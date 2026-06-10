"""
Medição empírica do tempo de execução do algoritmo guloso do rally.

Gera instâncias válidas de tamanho crescente e mede o tempo médio de
execução do guloso, evidenciando o crescimento linear O(n).
"""

import random
import time

from rally_greedy import greedy_paradas


def gera_instancia(n: int, d: float, rng: random.Random) -> tuple[float, list[float]]:
    pontos = []
    pos = 0.0
    for _ in range(n):
        pos += rng.uniform(0.1, d)
        pontos.append(pos)
    L = pontos[-1] + rng.uniform(0.0, d)
    return L, pontos


def mede(n: int, repeticoes: int = 5) -> tuple[float, int]:
    rng = random.Random(123)
    d = 10.0
    L, pontos = gera_instancia(n, d, rng)
    melhor = float("inf")
    paradas = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        paradas = greedy_paradas(L, d, pontos)
        fim = time.perf_counter()
        melhor = min(melhor, fim - inicio)
    return melhor, len(paradas)


if __name__ == "__main__":
    print(f"{'n':>12} {'tempo (s)':>12} {'tempo/n (us)':>14} {'paradas':>10}")
    for n in [1_000, 10_000, 100_000, 1_000_000, 5_000_000, 10_000_000]:
        t, k = mede(n)
        print(f"{n:>12,} {t:>12.6f} {t / n * 1e6:>14.4f} {k:>10,}")
