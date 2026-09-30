import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from matplotlib.lines import Line2D

st.title("Wiring Simulator")

threshold = st.slider("Similarity Threshold", min_value=0.8, max_value=0.99, value=0.915)
# metric = st.selectbox("Choose Metric", ["Degree", "Betweenness", "Clustering Coefficient"])

# code lines from 02-Notebooks/Phase-01/02-wiring.ipynb
node_labels = np.load('01-Dataset/node_labels.npy')
node_metrics = np.load('01-Dataset/node_metrics.npy')

similarity_mat = cosine_similarity(node_metrics) 

G = nx.Graph()
num_nodes = len(node_labels)

for i in range(0, num_nodes):
    G.add_node(i, label=node_labels[i])

for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if similarity_mat[i, j] >= threshold:
            G.add_edge(i, j)

fig, ax = plt.subplots(figsize=(10, 8)) # Newly added line
pos = nx.spring_layout(G, seed=42)

# Add conditions for the selectbox, according to the available options:
if metric == "Degree":
    metric_dict = nx.degree_centrality(G)
elif metric == "Betweenness":
    metric_dict = nx.betweeness_centrality(G)
else:
    metric_dict = nx.clustering(G)
    
node_sizes = [(metric_dict[node] * 1000) + 50 for node in G.nodes()] # Centrality scores: [0,1]; multiplying with 1000 to scale it up
    
color = ["#ff0000" if label == 0 else "#de00fc" if label == 1 else "#38F100" for label in node_labels]

nx.draw_networkx_nodes(G, pos, node_color=color, node_size=100)
nx.draw_networkx_edges(G, pos, alpha=0.2)
plt.title('The Network', fontsize=16)

profiles = [
    Line2D([0], [0], marker='o', color='w', label='Impulsive', markerfacecolor='#ff0000', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Analytical', markerfacecolor='#de00fc', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Gambler', markerfacecolor='#38F100', markersize=10),
]

plt.legend(handles=profiles, loc='upper right', title='Profiles')
plt.tight_layout()

# Pushing to streamlit
st.pyplot(fig)

