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
