"""
Testes de corretude do algoritmo guloso do rally.

Compara o número de paradas do guloso com a solução exata por programação
dinâmica em milhares de instâncias aleatórias válidas, além de casos de
borda escolhidos à mão.
"""

import random

from rally_greedy import greedy_paradas, otimo_paradas_dp, conjunto_valido


def gera_instancia_valida(rng: random.Random) -> tuple[float, float, list[float]]:
    """Gera (L, d, pontos) garantindo que o conjunto completo é válido.

    Constrói os pontos por incrementos no intervalo (0, d], de modo que a
    distância entre vizinhos (e do início ao primeiro ponto) nunca exceda d.
    """
    d = rng.uniform(1.0, 20.0)
    n = rng.randint(1, 40)
    pontos: list[float] = []
    pos = 0.0
    # incrementos estritamente menores que d para evitar que erros de
    # arredondamento de ponto flutuante tornem a instância inválida
    for _ in range(n):
        pos += rng.uniform(0.1, 0.95 * d)
        pontos.append(pos)
    # final a no máximo d do último ponto
    L = pontos[-1] + rng.uniform(0.0, 0.95 * d)
    return L, d, pontos


def testa_casos_de_borda() -> None:
    # chega ao final sem acampar
    assert greedy_paradas(10, 10, [5.0]) == []
    # precisa acampar exatamente uma vez
    assert greedy_paradas(20, 10, [10.0]) == [10.0]
    # distâncias exatamente iguais a d (caso limite de igualdade)
    assert greedy_paradas(30, 10, [10.0, 20.0]) == [10.0, 20.0]
    # vários pontos no mesmo dia: deve escolher sempre o mais distante
    assert greedy_paradas(19, 10, [2.0, 5.0, 9.0, 12.0]) == [9.0]
    # se o final ainda não é alcançável, acampa de novo no caminho
    assert greedy_paradas(20, 10, [2.0, 5.0, 9.0, 12.0]) == [9.0, 12.0]
    # exemplo em que parar "cedo demais" custaria uma parada extra
    assert len(greedy_paradas(25, 10, [4.0, 7.0, 9.0, 12.0, 16.0, 18.0, 21.0, 24.0])) == 2
    print("Casos de borda: OK")


def testa_contra_dp(n_instancias: int = 5000, semente: int = 42) -> None:
    rng = random.Random(semente)
    for k in range(n_instancias):
        L, d, pontos = gera_instancia_valida(rng)
        guloso = greedy_paradas(L, d, pontos)
        otimo = otimo_paradas_dp(L, d, pontos)
        assert guloso is not None, f"instancia {k}: guloso nao encontrou solucao"
        assert conjunto_valido(L, d, guloso), f"instancia {k}: solucao gulosa invalida"
        assert len(guloso) == len(otimo), (
            f"instancia {k}: guloso usou {len(guloso)} paradas, otimo usa {len(otimo)}\n"
            f"L={L} d={d} pontos={pontos}"
        )
    print(f"Comparacao com DP em {n_instancias} instancias aleatorias: OK "
          f"(guloso = otimo em todas)")


if __name__ == "__main__":
    testa_casos_de_borda()
    testa_contra_dp()
