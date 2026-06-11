import random
import time
from rally_greedy import greedy_paradas
#  gera uma instancia aleatoria com n pontos
def gera_instancia(n: int, d: float, rng: random.Random) -> tuple[float, list[float]]:
    pontos = []  # lista de posicoes dos pontos
    pos = 0.0
    for _ in range(n):
        pos += rng.uniform(0.1, d)           #  incremento sempre alcancavel
        pontos.append(pos)
    L = pontos[-1] + rng.uniform(0.0, d)  # final alcancavel a partir do ultimo ponto
    return L, pontos
# mede o tempo do guloso para um tamanho n
def mede(n: int, repeticoes: int = 5) -> tuple[float, int]:
    rng = random.Random(123)  #   semente fixa para reproduzir
    d = 10.0
    L, pontos = gera_instancia(n, d, rng)
    melhor = float("inf")       # guarda o menor tempo medido
    paradas = []
    for _ in range(repeticoes):     # repete para reduzir ruido de medicao
        inicio = time.perf_counter()
        paradas = greedy_paradas(L, d, pontos)  # executa o algoritmo
        fim = time.perf_counter()
        melhor = min(melhor, fim - inicio)  # fica com o melhor tempo
    return melhor, len(paradas)  # retorna tempo e numero de paradas
# roda o benchmark para varios tamanhos
if __name__ == "__main__":
    print(f"{'n':>12} {'tempo (s)':>12} {'tempo/n (us)':>14} {'paradas':>10}")
    # tamanhos crescentes de entrada
    for n in [1_000, 10_000, 100_000, 1_000_000, 5_000_000, 10_000_000]:
        t, k = mede(n)  # mede o tempo para esse n
        print(f"{n:>12,} {t:>12.6f} {t / n * 1e6:>14.4f} {k:>10,}")
