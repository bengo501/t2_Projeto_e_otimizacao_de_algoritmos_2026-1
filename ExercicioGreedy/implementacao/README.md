# Exercício Greedy — Rally pelo Deserto de Dakkar

Disciplina: Projeto e Otimização de Algoritmos — Prof. Michael da Costa Móra

Implementação em Python (3.8+, sem dependências externas) do algoritmo guloso
que escolhe o menor conjunto válido de pontos de parada para completar o rally.

## Arquivos

| Arquivo          | Conteúdo                                                            |
|------------------|---------------------------------------------------------------------|
| `rally_greedy.py`| Algoritmo guloso O(n), verificador exato por DP O(n²) e validador de conjuntos; executável com um exemplo. |
| `testes.py`      | Casos de borda + comparação do guloso com a DP exata em 5000 instâncias aleatórias válidas. |
| `benchmark.py`   | Medição do tempo de execução do guloso para n de 10³ a 10⁷ pontos.  |

## Como executar

```bash
python rally_greedy.py   # exemplo ilustrativo
python testes.py         # testes de corretude (guloso = ótimo em todas as instâncias)
python benchmark.py      # medição de tempo (evidencia crescimento linear)
```
