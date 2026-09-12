# Behavioral Homophily Network: Development Cycles

---

## Cycle 1: Baseline Topology and Wiring

* **Setup**:
  * Generation of synthetic network of `150` nodes using three distinct `baseline` psychological profiles.
  * Wiring the topology using a similarity matrix(`cosine similarity`)[from `sklearn.metrics.pairwise`]
* **Parameters Used**:
  * Profiles:

    ```py
    # Features: [Risk Tolerance, Observation Index, Impulsivity]
    0: [0.7, 0.2, 0.95],  # Impulsive
    1: [0.47, 0.9, 0.32], # Analytical
    2: [0.9, 0.87, 0.5]   # Gambler
    ```

  * `similarity_threshold = 0.90`
  * `layout = nx.spring_layout(G, seed=42)`
* **Observations**:
  * **Outcome**: The wiring did not form three perfectly isolated clusters as per the initial hypothesis.
  * **Insight**: The `Analytical` and `Gambler` profiles formed dense links.

  ---

  ### Cycle 2: Restructuring the Toplogy

  * **Modifications**: Updated metrics for the different psychological labels.
  * **Parameters Used**:
    * Profiles:

    ```py
      # Features: [Risk Tolerance, Observation Index, Impulsivity]
      0: [0.87, 0.12, 0.95], # Impulsive: Extreme Risk Tolerance and Impulsiveness, Low observation
      1: [0.2, 0.97, 0.20],  # Analytical: Extreme Observation, Lower Risk Tolerance and Impulsiveness
      2: [0.73, 0.59, 0.65]  # Gambler: High Risk, Moderate Obseration(Acts as a middle ground)

    ```

    * `similarity_threshold = 0.915`(+0.015)
  * **Outcome**: Achieved a more realistic and messy topological network.
  * **Insights**: `Impulsive` and `Gambler` profiles have stronger links when compared to `Analytical` one.
  
  ---

  ### Cycle 3: Embedding

  * **Setup**:
    * **Node2Vec**: Used to flatten the graph into a `150 x 64` matrix.
  * **Parameters Used**:
    * `dimensions=64`
    * `walk_length=30`
    * `num_walks=200`
    * `window=10`

  * **Visualization**:
    * **PCA**:
      * **Parameters Used**:
        * `n_components=2`
        * `random_state=42`
      * **Inference**:
        * **Analytical**: Pushed entirely to the far left of the X-axis. This separation confirms `Analytical` profiles form an 'Echo-Chamber'.
        * **Impulsive & Gambler**: Occupy the same X-axis territory on the right. PCA algorithm was forced to separate them based on Y-axis due to their strong links to slice them apart, since `Node2Vec` maps based on network topology.
        * **Bridge**: The outliers labelled as `Analytical` have been observed to act as rare bridges between the dominant profiles.
    * **t-SNE**:
      * **Parameters Used**:
        * `n_components=2`
        * `perplexity=30`
        * `max_iter=1000`
        * `random_state=42`
      * **Inference**:
        * **Analytical**: Forms a highly isolated cluster spaced far apart from `Impulsive` and `Gambler`. Zero cross profile links.
        * **Impulsive & Gambler**: `t-SNE` algorithm has successfully segregated these two inter-twined profiles into distinct clusters.
        * **Bridge**: There is no bridge to link the `Analytical` ones, forming a closed loop 'Echo Chamber'. `Impulsive` and `Gambler` profiles have weak bridges, somewhat showing a degree of correlation.
