# Principal Component Analysis (PCA)

A theoretical guide to PCA, from intuition to a fully worked example by hand.

---

## 1. What is PCA?

**Principal Component Analysis** is an unsupervised, linear technique for **dimensionality reduction**. It takes a dataset with many (possibly correlated) features and finds a new set of axes, called **principal components (PCs)**, such that:

- Each PC is a **linear combination** of the original features.
- PCs are **orthogonal** (uncorrelated) to each other.
- PC1 points in the direction of **maximum variance** in the data, PC2 captures the maximum *remaining* variance while being orthogonal to PC1, and so on.

By keeping only the first *k* components, we compress the data while retaining as much of its variability ("information") as possible.

---

## 2. Intuition

Imagine a cloud of points shaped like a tilted ellipse. The original axes (x, y) don't line up with the shape of the cloud. PCA **rotates the coordinate system** so that:

- The first new axis runs along the **long side** of the ellipse (most spread).
- The second new axis runs along the **short side** (least spread).

If the short side is very thin, we can drop it and describe each point with just one number, its position along the long axis, losing very little.

---

## 3. Why use PCA?

| Purpose | How PCA helps |
|---|---|
| Dimensionality reduction | Fewer features → faster models, less storage |
| Removing multicollinearity | PCs are uncorrelated by construction |
| Visualization | Project high-dimensional data to 2D/3D |
| Noise reduction | Low-variance components often carry mostly noise |
| Combating the curse of dimensionality | Fewer dimensions → denser data, better generalization |

---

## 4. Key Concepts

- **Variance**: how spread out a single feature is.
- **Covariance**: how two features vary together. Positive → they increase together; negative → one increases as the other decreases.
- **Covariance matrix (Σ)**: a *d × d* symmetric matrix holding all pairwise covariances; variances sit on the diagonal.
- **Eigenvector**: a direction that the covariance matrix only stretches, not rotates. These are the **principal component directions**.
- **Eigenvalue (λ)**: the amount of variance captured along its eigenvector.
- **Explained variance ratio**: λᵢ / Σλ, the fraction of total variance captured by PC *i*.

---

## 5. The Algorithm (Step by Step)

Given a data matrix **X** with *n* samples and *d* features:

1. **Center the data**: subtract the mean of each feature so every feature has mean 0.
   `X_c = X − μ`
2. **(Optional) Standardize**: divide each feature by its standard deviation if features are on different scales (e.g., cm vs kg). Otherwise, large-scale features dominate.
3. **Compute the covariance matrix**:
   `Σ = (1 / (n − 1)) · X_cᵀ X_c`
4. **Eigen-decomposition**: solve `Σ v = λ v` to get eigenvalues λ₁ ≥ λ₂ ≥ … ≥ λ_d and their eigenvectors v₁, v₂, …, v_d.
5. **Sort and select**: order components by eigenvalue (descending) and choose the top *k*.
6. **Project**: form **W** = [v₁ … v_k] (a *d × k* matrix) and compute the new data:
   `Z = X_c · W`

**Reconstruction** (approximate) back to the original space:
`X̂ = Z · Wᵀ + μ`

> In practice, libraries often use **Singular Value Decomposition (SVD)** of X_c instead of explicitly forming Σ. It gives the same components and is more numerically stable.

---

## 6. Worked Example (By Hand)

### 6.1 The data

Five samples, two features (same units, so no standardization needed):

| Sample | x₁ | x₂ |
|:--:|:--:|:--:|
| A | 6 | 8 |
| B | 2 | 4 |
| C | 5 | 5 |
| D | 3 | 7 |
| E | 4 | 6 |

### 6.2 Step 1: Center the data

Means: μ₁ = (6+2+5+3+4)/5 = **4**, μ₂ = (8+4+5+7+6)/5 = **6**

| Sample | x₁ − 4 | x₂ − 6 |
|:--:|:--:|:--:|
| A | 2 | 2 |
| B | −2 | −2 |
| C | 1 | −1 |
| D | −1 | 1 |
| E | 0 | 0 |

### 6.3 Step 2: Covariance matrix

With n − 1 = 4:

- Var(x₁) = (4 + 4 + 1 + 1 + 0) / 4 = **2.5**
- Var(x₂) = (4 + 4 + 1 + 1 + 0) / 4 = **2.5**
- Cov(x₁, x₂) = (4 + 4 − 1 − 1 + 0) / 4 = **1.5**

```
Σ = | 2.5  1.5 |
    | 1.5  2.5 |
```

The positive covariance tells us x₁ and x₂ tend to rise together.

### 6.4 Step 3: Eigenvalues

Solve det(Σ − λI) = 0:

```
(2.5 − λ)² − 1.5² = 0
2.5 − λ = ±1.5
λ₁ = 4,   λ₂ = 1
```

### 6.5 Step 4: Eigenvectors

- For λ₁ = 4: (2.5 − 4)a + 1.5b = 0 → a = b → **v₁ = (1, 1) / √2 ≈ (0.707, 0.707)**
- For λ₂ = 1: (2.5 − 1)a + 1.5b = 0 → a = −b → **v₂ = (1, −1) / √2 ≈ (0.707, −0.707)**

Check: v₁ · v₂ = 0.5 − 0.5 = 0 ✔ (orthogonal)

**Interpretation**
- **PC1** ≈ "overall size": an equal-weighted sum of x₁ and x₂.
- **PC2** ≈ "contrast": the difference between x₁ and x₂.

### 6.6 Step 5: Explained variance

| Component | Eigenvalue | Explained variance |
|:--:|:--:|:--:|
| PC1 | 4 | 4 / 5 = **80%** |
| PC2 | 1 | 1 / 5 = **20%** |

Total variance is preserved: 2.5 + 2.5 = 4 + 1 = 5.

### 6.7 Step 6: Project the data

Scores: z₁ = (x₁ + x₂)/√2 and z₂ = (x₁ − x₂)/√2 using centered values.

| Sample | Centered | PC1 score (z₁) | PC2 score (z₂) |
|:--:|:--:|:--:|:--:|
| A | (2, 2) | 4/√2 ≈ **2.83** | 0 |
| B | (−2, −2) | ≈ **−2.83** | 0 |
| C | (1, −1) | 0 | ≈ **1.41** |
| D | (−1, 1) | 0 | ≈ **−1.41** |
| E | (0, 0) | 0 | 0 |

Sanity check: variance of the PC1 scores = (8 + 8) / 4 = 4 = λ₁ ✔, and of PC2 = (2 + 2) / 4 = 1 = λ₂ ✔.

### 6.8 Reducing to 1 dimension

Keep only PC1 → each sample is now described by **one** number (z₁) and we retain **80%** of the variance.

Reconstructing from PC1 alone (X̂ = z₁ · v₁ᵀ + μ):

| Sample | Original | Reconstructed | Lost? |
|:--:|:--:|:--:|:--:|
| A | (6, 8) | (6, 8) | No, lies exactly on PC1 |
| B | (2, 4) | (2, 4) | No |
| C | (5, 5) | (4, 6) | Yes, its info was all in PC2 |
| D | (3, 7) | (4, 6) | Yes |
| E | (4, 6) | (4, 6) | No, it is the mean |

The 20% of variance we dropped corresponds exactly to C and D's deviations along PC2.

---

## 7. Choosing the Number of Components (k)

- **Cumulative explained variance**: keep enough PCs to reach a threshold (commonly 90–95%).
- **Scree plot**: plot eigenvalues in descending order and look for the "elbow" where the curve flattens.
- **Kaiser criterion**: (for standardized data) keep components with λ > 1.
- **Task-driven**: choose k by downstream model performance (e.g., cross-validation).

---

## 8. Assumptions and Limitations

- **Linearity**: PCA only finds linear structure. For curved manifolds, consider Kernel PCA, t-SNE, or UMAP.
- **Variance = importance**: high variance is assumed to be signal; this isn't always true.
- **Scale sensitivity**: always standardize when features have different units.
- **Outlier sensitivity**: outliers can heavily skew components (see Robust PCA).
- **Interpretability**: PCs are mixtures of features and can be hard to explain.
- **Unsupervised**: PCA ignores labels; the most variant direction may not be the most predictive (see LDA for a supervised alternative).

---

## 9. Summary

| Step | Operation | Result in example |
|---|---|---|
| 1 | Center data | Mean = (4, 6) |
| 2 | Covariance matrix | [[2.5, 1.5], [1.5, 2.5]] |
| 3 | Eigenvalues | 4, 1 |
| 4 | Eigenvectors | (1,1)/√2, (1,−1)/√2 |
| 5 | Explained variance | 80%, 20% |
| 6 | Project to k = 1 | 2D → 1D, 80% variance retained |

**PCA in one line:** rotate the data onto the directions of greatest variance, then drop the directions that carry little.