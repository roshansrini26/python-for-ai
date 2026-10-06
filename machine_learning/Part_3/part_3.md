# K-Means Clustering

## What is it?

K-Means is an **unsupervised learning** algorithm that groups unlabeled data into *k* clusters. Points in the same cluster are similar to each other, and different from points in other clusters. No target labels are used — the algorithm discovers structure on its own.

## Key Idea

Each cluster is represented by a **centroid** (the mean of its points). Every data point belongs to the cluster whose centroid is nearest, usually measured by **Euclidean distance**.

## Objective

K-Means minimises the **Within-Cluster Sum of Squares (WCSS)**, also called *inertia*:

$$
J = \sum_{i=1}^{k} \sum_{x \in C_i} \lVert x - \mu_i \rVert^2
$$

where $C_i$ is the *i*-th cluster and $\mu_i$ is its centroid. Lower *J* means tighter, more compact clusters.

## Algorithm (Lloyd's Algorithm)

1. **Choose k** — the number of clusters.
2. **Initialise** k centroids (randomly, or with *k-means++* for better starting points).
3. **Assignment step** — assign each point to its nearest centroid.
4. **Update step** — recompute each centroid as the mean of the points assigned to it.
5. **Repeat** steps 3–4 until centroids stop changing (convergence) or a maximum number of iterations is reached.

The algorithm always converges, but possibly to a **local minimum**, so it is often run several times with different initialisations.

## Choosing k

- **Elbow Method** — plot WCSS against k; the "elbow" where improvement slows is a good choice.
- **Silhouette Score** — measures how well each point fits its own cluster versus the nearest other cluster (range −1 to 1; higher is better).
- **Domain knowledge** — sometimes k is known from the problem itself.

## Advantages

- Simple and easy to interpret
- Fast and scalable to large datasets — roughly O(n · k · t) for n points and t iterations
- Works well when clusters are compact and well separated

## Limitations

- k must be specified in advance
- Sensitive to initial centroid placement
- Sensitive to outliers (means are pulled by extreme values)
- Assumes spherical, similarly sized clusters; struggles with irregular shapes
- Requires feature scaling, since it is distance-based

## Applications

- Customer segmentation
- Image compression and colour quantisation
- Document and topic grouping
- Anomaly detection
- Pattern discovery in sensor or biological data

## Summary

K-Means partitions data into k groups by repeatedly assigning points to the nearest centroid and updating centroids, minimising within-cluster variance. It is one of the most widely used clustering methods thanks to its simplicity and speed, though it works best on well-separated, roughly spherical clusters.