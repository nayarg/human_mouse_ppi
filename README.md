# Human Mouse PPI

Repository containing the embedding and distance data for the 2022 STRING human and mouse PPI networks

`/dist` folder contains the numpy distance matrices
- `cosine_human.npy` contains the cosine distances for the human proteins
- `cosine_mouse.npy` contains the cosine distance for the mouse proteins
- `cosine_human_mouse_edge.npy` contains the cosine distances for the human and mouse proteins embedding together with an edge between ALL orthologs
    - `cosine_edge_{threshold}.npy` contains the cosine distances for the human and mouse proteins embedded together with an edge between `{threshold}` percent of orthologs
- `cosine_human_mouse.npy` contains the cosine distance for the human and mouse proteins embedded together with no edge between orthologs



