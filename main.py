import networkx as nx
from networkx import DiGraph
import matplotlib.pyplot as plt

G1: DiGraph = nx.DiGraph()
G1.add_node(0)
G1.add_node(1)
G1.add_node(2)
G1.add_node(3)
G1.add_node(4)

G1.add_edge(0, 4, weight=2)
G1.add_edge(0, 2, weight=3)
G1.add_edge(0, 1, weight=5)
G1.add_edge(1, 3, weight=6)
G1.add_edge(1, 2, weight=2)
G1.add_edge(2, 1, weight=1)
G1.add_edge(2, 3, weight=2)
G1.add_edge(4, 1, weight=6)
G1.add_edge(4, 2, weight=10)
G1.add_edge(4, 3, weight=4)

def uzaklikVeBilgi(G):
    for i in range(4):
        try:
            sp = nx.dijkstra_path(G1, source=4, target=i)
            print(sp)
        except:
            print("Yol bulunamadı")

    weight = nx.get_edge_attributes(G1, 'weight')
    layout = nx.spring_layout(G1)
    nx.draw(G1, layout, with_labels=True)
    nx.draw_networkx_edge_labels(G1, layout, weight)
    plt.show()

print("4 numaralı düğümden tüm diğer düğümlere en kısa yol uzunlukları: ")
uzaklikVeBilgi(G1)
G1.remove_node(3)
print("3 numaralı düğüm silindikten sonra 4 numaralı düğümden tüm diğer düğümlere en kısa yol uzunlukları: ")
uzaklikVeBilgi(G1)