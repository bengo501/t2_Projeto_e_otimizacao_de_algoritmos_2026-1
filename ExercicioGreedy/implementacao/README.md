# Greedy
Projeto e Otimização de Algoritmos
Prof. Michael da Costa Móra

Algoritmo guloso que escolhe o menor conjunto válido de pontos de parada para completar o rally em python

## Arquivos
| Arquivo          | Conteúdo                                                            |
|------------------|---------------------------------------------------------------------|
| `rally_greedy.py`| Algoritmo guloso O(n), verificador exato por DP O(n²) e validador de conjuntos. Executável com um exemplo. |
| `testes.py`      | Casos de borda + comparação do guloso com a DP exata em 5000 instâncias aleatórias válidas. |
| `benchmark.py`   | Medição do tempo de execução do guloso para n de 10³ a 10⁷ pontos.  |

## Como executar
```bash
python rally_greedy.py   # exemplo 
python testes.py         # testes de corretude (guloso = ótimo em todas as instâncias)
python benchmark.py      # medição de tempo (evidencia de crescimento linear)
```
