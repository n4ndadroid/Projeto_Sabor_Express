# 🚀 Rota Inteligente: Otimização de Entregas para "Sabor Express"

[cite_start]Este projeto foi desenvolvido como parte da disciplina "Artificial Intelligence Fundamentals" da UniFECAF[cite: 1, 15].

## [cite_start]1. Descrição do Problema, Desafio e Objetivos [cite: 51]

* [cite_start]**Empresa:** Sabor Express, uma pequena empresa de delivery de alimentos[cite: 6].
* [cite_start]**Desafio:** A empresa enfrenta grandes desafios em horários de pico[cite: 7], resultando em:
    * [cite_start]Rotas ineficientes[cite: 8].
    * [cite_start]Atrasos nas entregas[cite: 8].
    * [cite_start]Aumento no custo de combustível[cite: 8].
    * [cite_start]Insatisfação dos clientes[cite: 8].
* [cite_start]**Causa Raiz:** O planejamento de rotas é feito manualmente, baseado apenas na experiência dos entregadores, sem apoio tecnológico[cite: 10].
* [cite_start]**Objetivo:** Desenvolver uma solução inteligente baseada em IA [cite: 11] capaz de:
    1.  [cite_start]Agrupar entregas próximas (clustering)[cite: 18].
    2.  [cite_start]Encontrar o menor caminho (rota) entre múltiplos pontos de entrega[cite: 13].
    3.  [cite_start]Tornar as entregas mais rápidas, eficientes e econômicas[cite: 9].

## [cite_start]2. Abordagem Adotada [cite: 52]

[cite_start]Para solucionar o desafio, a cidade foi modelada como um **grafo**, onde os locais de entrega são os "nós" e as ruas são as "arestas" com pesos (distância/tempo)[cite: 12].

[cite_start]A solução foi dividida em duas etapas principais, conforme sugerido pelo desafio[cite: 18, 19]:

1.  **Etapa 1: Agrupamento de Pedidos (Clustering)**
    * [cite_start]Em momentos de alta demanda [cite: 14][cite_start], os pedidos recebidos são primeiro agrupados por proximidade geográfica usando o algoritmo **K-Means**[cite: 19].
    * Isso cria "zonas" de entrega, permitindo que um único entregador atenda a vários pedidos em uma mesma viagem, otimizando o esforço.

2.  **Etapa 2: Otimização de Rota (Pathfinding)**
    * Após a definição dos clusters (ou para entregas individuais), aplicamos um algoritmo de busca em grafo para encontrar o caminho mais eficiente.
    * [cite_start]O algoritmo escolhido foi o **$A^{*}$ (A-Estrela)**[cite: 19], pois ele é ideal para encontrar o menor caminho em grafos com pesos (como um mapa com distâncias).

[cite_start]Esta abordagem é inspirada em soluções de mercado robustas, como o sistema **ORION da UPS** [cite: 24][cite_start], que também utiliza algoritmos e heurísticas para otimizar rotas e gerar economias significativas[cite: 25, 26].

## [cite_start]3. Algoritmos Utilizados [cite: 53]

[cite_start]Foram utilizados os seguintes algoritmos clássicos de IA[cite: 48]:

### a. K-Means (Aprendizado Não Supervisionado)

* **Objetivo:** Agrupar entregas próximas[cite: 18, 35].
* **Por que o K-Means?** É um algoritmo eficiente e simples de implementar para particionar dados (nossos pontos de entrega) em 'K' grupos distintos (as zonas de entrega). Ele tenta minimizar a distância entre os pontos dentro de um mesmo grupo, o que é exatamente o que queremos.
* **Como funciona:**
    1.  Definimos 'K' (o número de entregadores/zonas).
    2.  O algoritmo posiciona 'K' centróides aleatoriamente.
    3.  Ele atribui cada ponto de entrega ao centróide mais próximo.
    4.  Ele recalcula a posição do centróide para ser o centro médio de todos os pontos atribuídos a ele.
    5.  Repete os passos 3 e 4 até que os grupos não mudem mais.

### b. Algoritmo $A^{*}$ (A-Estrela) (Busca Heurística)

* **Objetivo:** Encontrar o menor caminho entre o restaurante e os pontos de entrega (dentro de um cluster)[cite: 13, 19].
* [cite_start]**Por que o $A^{*}$?** O desafio pede um algoritmo de busca eficiente[cite: 13, 19]. Vamos comparar:
    * **BFS (Busca em Largura):** Encontra o caminho mais curto em *número de paradas*, mas ignora os "pesos" (distância/tempo). Em um mapa real, o caminho com menos ruas não é, necessariamente, o mais rápido.
    * **DFS (Busca em Profundidade):** Explora um caminho até o fim antes de tentar outro. É muito ineficiente para mapas e não garante o menor caminho.
    * **$A^{*}$ (A-Estrela):** É a escolha ideal. Ele é um algoritmo "informado", pois usa uma **heurística** (uma estimativa inteligente da distância até o objetivo). Ele equilibra o custo do caminho já percorrido com o custo estimado que falta, explorando os caminhos mais promissores primeiro. Isso o torna muito mais rápido e eficiente que o BFS para problemas de rota.

## [cite_start]4. Diagrama do Grafo / Modelo da Solução [cite: 54]

*(Insira aqui uma imagem do seu grafo. Pode ser um print do seu código (usando bibliotecas como Matplotlib ou NetworkX) ou um diagrama simples que você desenhou).*

**Exemplo de Grafo da Cidade (Modelo Simplificado):**

(10 min)
(Restaurante) ---- (Bairro A) |

(5 min)| \ (8 min) |

(Bairro B) --- (Bairro C) (4 min)


`![Diagrama do Grafo](link_para_sua_imagem.png)`

## 5. Análise dos Resultados, Limitações e Melhorias [cite: 55]

### Análise de Eficiência
*(Aqui você deve mostrar seus resultados. Ex: "Para um cenário com 10 entregas, a rota manual teria 45 km. Usando K-Means (K=2) e $A^{*}$, dividimos em duas rotas de 12 km e 15 km, totalizando 27 km, uma economia de 40%").*

*(Insira prints do seu código em ação, mostrando os clusters e as rotas traçadas).*

### Limitações Encontradas
* **Grafo Estático:** A solução atual utiliza um grafo com pesos fixos (distância). Ela não considera fatores dinâmicos como trânsito em tempo real, acidentes ou horários de pico (que era parte do desafio original [cite: 7]).
* **Definição do 'K':** O número de clusters (K) no K-Means precisa ser definido manualmente.

### Sugestões de Melhoria
* **Roteamento Dinâmico:** Integrar com uma API (como Google Maps) para obter dados de tráfego em tempo real, similar ao que artigos sugerem[cite: 37].
* **Algoritmos Avançados:** Explorar algoritmos heurísticos mais avançados (como Algoritmos Genéticos) ou Aprendizado por Reforço (RL) [cite: 37, 38] para otimização contínua, como visto nos casos de estudo[cite: 40].
