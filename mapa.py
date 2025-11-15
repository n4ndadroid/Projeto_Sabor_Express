import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo_cidade():
    """
    Cria um grafo representando o mapa da "Sabor Express".
    Os nós são locais (Restaurante, Bairros) e as arestas
    são as ruas com pesos (distância/tempo).
    """
    # Criar um grafo
    G = nx.Graph()

    # Adicionar os nós (locais)
    G.add_node("Restaurante")
    G.add_node("Bairro A")
    G.add_node("Bairro B")
    G.add_node("Bairro C")
    G.add_node("Bairro D")
    G.add_node("Bairro E")

    # Adicionar as arestas (ruas) com pesos (distância/tempo)
    # 
    G.add_edge("Restaurante", "Bairro A", weight=5)
    G.add_edge("Restaurante", "Bairro B", weight=8)
    G.add_edge("Bairro A", "Bairro C", weight=3)
    G.add_edge("Bairro A", "Bairro B", weight=4)
    G.add_edge("Bairro B", "Bairro D", weight=7)
    G.add_edge("Bairro C", "Bairro D", weight=6)
    G.add_edge("Bairro C", "Bairro E", weight=10)
    G.add_edge("Bairro D", "Bairro E", weight=2)
    
    print("Grafo da cidade criado com sucesso!")
    return G

def desenhar_grafo(G):
    """
    Desenha o grafo para visualização.
    Isso é útil para o seu README.
    """
    pos = nx.spring_layout(G, seed=42)  # Posições para os nós
    labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Diagrama do Grafo - Sabor Express")
    
    # Salvar a imagem para o README 
    plt.savefig("diagrama_grafo.png")
    print("Imagem 'diagrama_grafo.png' salva.")
    plt.show()

# --- Execução principal ---
if __name__ == "__main__":
    mapa_cidade = criar_grafo_cidade()
    desenhar_grafo(mapa_cidade)
