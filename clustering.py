import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Simular pontos de entrega (pedidos)
# Em um projeto real, seriam coordenadas (latitude/longitude)
# Vamos usar coordenadas (x, y) simples para este exemplo.
pontos_de_entrega = [
    (2, 3), (3, 3), (1, 2),  # Cluster 1 (perto)
    (10, 8), (9, 9), (11, 8), # Cluster 2 (longe)
    (2, 10), (1, 9), (3, 11)  # Cluster 3 (outro lado)
]

# Converter para um formato que o K-Means entende
# (uma lista de listas ou array NumPy)
dados = [[p[0], p[1]] for p in pontos_de_entrega]

# 2. Aplicar o K-Means 
# Vamos supor que temos 3 entregadores (K=3)
K = 3
kmeans = KMeans(n_clusters=K, random_state=42, n_init=10)
kmeans.fit(dados)

# 3. Obter os resultados
labels = kmeans.labels_
centros = kmeans.cluster_centers_

print(f"Rótulos dos clusters: {labels}")
# Ex: [0 0 0 1 1 1 2 2 2] -> os 3 primeiros são do cluster 0, etc.

# 4. Visualizar os clusters (para seu README/Vídeo) [cite: 59]
plt.figure(figsize=(8, 6))
# 'zip(*pontos_de_entrega)' separa as coordenadas x e y
x_coords, y_coords = zip(*pontos_de_entrega)

# Desenha os pontos de entrega, coloridos por cluster
plt.scatter(x_coords, y_coords, c=labels, cmap='viridis', s=100, alpha=0.8)

# Desenha os centros dos clusters
plt.scatter(centros[:, 0], centros[:, 1], c='red', s=250, marker='X', label='Centros (Zonas)')

plt.title("Agrupamento de Pedidos com K-Means")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.legend()
plt.savefig("clusters_kmeans.png") # Salvar imagem [cite: 59]
print("Imagem 'clusters_kmeans.png' salva.")
plt.show()
