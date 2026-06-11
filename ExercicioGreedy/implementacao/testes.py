import random
from rally_greedy import greedy_paradas, otimo_paradas_dp, conjunto_valido
# gera uma instancia aleatoria sempre resolvivel
def gera_instancia_valida(rng: random.Random) -> tuple[float, float, list[float]]:
    d = rng.uniform(1.0, 20.0)
    n = rng.randint(1, 40)
    pontos: list[float] = []
    pos = 0.0
    for _ in range(n):
        pos += rng.uniform(0.1, 0.95 * d)          # incremento menor que d para evitar erro de arredondamento
        pontos.append(pos)
    L = pontos[-1] + rng.uniform(0.0, 0.95 * d)  #  final a no maximo d do ultimo ponto
    return L, d, pontos
# testa situacoes limite do algoritmo
def testa_casos_de_borda() -> None:
    assert greedy_paradas(10, 10, [5.0]) == []                            #    chega ao final sem acampar
    assert greedy_paradas(20, 10, [10.0]) == [10.0]                       #    precisa acampar exatamente uma vez
    assert greedy_paradas(30, 10, [10.0, 20.0]) == [10.0, 20.0]           #    distancias exatamente iguais a d
    assert greedy_paradas(19, 10, [2.0, 5.0, 9.0, 12.0]) == [9.0]        #     varios pontos no mesmo dia escolhe o mais distante
    assert greedy_paradas(20, 10, [2.0, 5.0, 9.0, 12.0]) == [9.0, 12.0]  #  final ainda longe entao acampa de novo
    assert len(greedy_paradas(25, 10, [4.0, 7.0, 9.0, 12.0, 16.0, 18.0, 21.0, 24.0])) == 2  # parar cedo demais custaria parada extra
    print("Casos de borda: OK")
# compara o guloso com o otimo em instancias aleatorias
def testa_contra_dp(n_instancias: int = 5000, semente: int = 42) -> None:
    rng = random.Random(semente)  # gerador com semente fixa para reproduzir
    for k in range(n_instancias):  # repete para varias instancias
        L, d, pontos = gera_instancia_valida(rng)     #  cria uma instancia valida
        guloso = greedy_paradas(L, d, pontos)         #  resposta do guloso
        otimo = otimo_paradas_dp(L, d, pontos)        #  resposta otima da dp
        assert guloso is not None, f"instancia {k}: guloso nao encontrou solucao"
        assert conjunto_valido(L, d, guloso), f"instancia {k}: solucao gulosa invalida"
        assert len(guloso) == len(otimo), (  # guloso deve usar o mesmo numero de paradas que o otimo
            f"instancia {k}: guloso usou {len(guloso)} paradas, otimo usa {len(otimo)}\n"
            f"L={L} d={d} pontos={pontos}"
        )
    print(f"Comparacao com DP em {n_instancias} instancias aleatorias: OK "
          f"(guloso = otimo em todas)")
# executa todos os testes
if __name__ == "__main__":
    testa_casos_de_borda()  # testa situacoes limite do algoritmo
    testa_contra_dp()  # compara o guloso com o otimo em instancias aleatorias
