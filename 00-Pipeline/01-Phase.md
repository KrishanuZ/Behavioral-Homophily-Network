#

## Phase: The Academic PoC (Low Friction)

Instead of processing massive real-world datasets, you use a lightweight, synthetic dataset that models how different personalities interact and group together based on psychological traits.

* The Node Features: You generate 100–200 "user" nodes. Instead of financial data, their features are numeric scores based on behavioral psychology:

  * Risk Tolerance (Are they playing in the rain or staying in the shed?)
  * Observational Index (Analytical vs. Reactive)
  * Social Proximity (Introversion vs. Extraversion)

* The Graph Architecture (Edges): Edges are drawn between nodes based on "Homophily"—the psychological principle that similar people cluster together. If two nodes have a high cosine similarity in their behavioral scores, they share an edge.

* The ML Task: You run an Unsupervised Graph Learning algorithm (satisfying Lab 2 or Lab 4) or standard Community Detection (Unit V). The model's job is to automatically cluster these nodes into distinct "Personality Archetypes" without you telling it what those archetypes are.

## Why this is a tactical masterstroke for her lab

During the presentation, you can explicitly mention that the node features were inspired by situational risk-assessment models—exactly like asking primary students how they react to rain on a playground. You are mathematically proving the psychological profiling she was doing manually in the first lab. She will instantly recognize the callback to her own methodology.
