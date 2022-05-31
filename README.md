# Human Mouse PPI

Repository containing the embedding and distance data for the 2022 STRING human and mouse PPI networks

`/embedding` folder contains the output of the embedding algorith
- The relevant files to the cosine distance calculation are `node_id_{type}.npy` (where type is either human, mouse, human mouse with edge, human mouse without edge) and `node_vectors_{type}.npy`. The `node_id` file contains a list of the protein names and `node_vectors` contains the vector for each protein, using the same order as the `node_id` list. 
- The `human_id_vector.csv` file contains the combined name and vector 


`/dist` folder contains the numpy distance matrices
- `cosine_human.npy` contains the cosine distances for the human proteins
- `cosine_mouse.npy` contains the cosine distance for the mouse proteins
- `cosine_human_mouse_edge.npy` contains the cosine distances for the human and mouse proteins embedding together with an edge between ALL orthologs
    - `cosine_edge_{threshold}.npy` contains the cosine distances for the human and mouse proteins embedded together with an edge between `{threshold}` percent of orthologs
- `cosine_human_mouse.npy` contains the cosine distance for the human and mouse proteins embedded together with no edge between orthologs

