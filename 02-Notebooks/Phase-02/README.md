# Behavioral Homophily Network: Development Cycle-Phase 02

## Cycle 1: Network Analytics and Centrality Metrics

* **Setup**: Visualization of Network Centrality Metrics using **Violin Plots**.
* **Parameters**: `Degree Centrality`, `Betweenness`, and `Clustering Coefficient`.
* **Inference**:
  * **Degree Centrality**: `Gambler` and `Impulsive` nodes act as **central hub** for links. The `Analytical` nodes have stricter links, maintaining very few connections.
  * **Betweenness**: Majority of nodes have zero links with the other profiles. However, the outliers in the `Analytical` profile act as the **weak ties**, serving as bridges.
  * **Clustering Coefficient**: Since `Analytical` cluster is a **closed loop**, the resultant Clustering Coefficient is very high.

![Centrality Metrics](centrality_metrics.png)
