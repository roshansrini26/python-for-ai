# Machine Learning

## Supervised Learning
Uses labeled inputs (meaning the input has a corresponding output label) to train models and learn outputs

### Feature
- Qualitative: categorical data(finite number of categories or groups)
    - Nominal data (no inherent order) eg, Male female, Countries
    - Ordinal data. (inherent order) eg, Rating good bad

**One hot Encoding**
eg [USA,India,Canada, France]
USA - [1,0,0,0]
India - [0,1,0,0]
Canada - [0,0,1,0]
France - [0,0,0,1]

- Quantitative: numerical valued data (could be discrete or continous)

### Supervised learning tasks
- Classification: predict discrete classes
    - Binary classification: Positive/negative, Cat/dog, Spam/not spam
    - Multiclass classification: Plant species, Animal

- Regression: predict continous values

## Unsupervised learning
Uses unlabeled data to learn about patterns in data

## Reinforcement Learning 
Agent learning in interactive environment based on rewards and penalties

## Metrics of Performance
**Loss: Actual - Predicted**

### L1 Loss (Mean Absolute Error)

$$
L_1 = \frac{1}{n} \sum_{i=1}^{n} \left| y_i - \hat{y}_i \right|
$$

### L2 Loss (Mean Squared Error)

$$
L_2 = \frac{1}{n} \sum_{i=1}^{n} \left( y_i - \hat{y}_i \right)^2
$$

where $y_i$ is the true value, $\hat{y}_i$ is the predicted value, and $n$ is the number of samples.

### Binary Cross-Entropy Loss

$$
L_{BCE} = -\frac{1}{n} \sum_{i=1}^{n} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
$$

where $y_i \in \{0, 1\}$ is the true label and $\hat{y}_i \in (0, 1)$ is the predicted probability.

Loss decreases as the performace gets better

## Models

### K Nearest Neighbour

#### Euclidean Distance

Between two points $\mathbf{p} = (p_1, p_2, \dots, p_n)$ and $\mathbf{q} = (q_1, q_2, \dots, q_n)$:

$$
d(\mathbf{p}, \mathbf{q}) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2}
$$

In two dimensions this reduces to:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

- In a N-dimension the new point calculates the distances of other points which (k depends) to predict the probabilty of the outcome

### Naive bayes theorem

### Conditional Probability

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0
$$

Rearranged, this gives the multiplication rule:

$$
P(A \cap B) = P(A \mid B) \, P(B) = P(B \mid A) \, P(A)
$$

### Bayes' Rule

$$
P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}
$$

Expanding the denominator with the law of total probability:

$$
P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B \mid A) \, P(A) + P(B \mid \neg A) \, P(\neg A)}
$$

For a partition $\{A_1, A_2, \dots, A_n\}$ of the sample space:

$$
P(A_k \mid B) = \frac{P(B \mid A_k) \, P(A_k)}{\sum_{i=1}^{n} P(B \mid A_i) \, P(A_i)}
$$

### Logistic regression

### From a Linear Model to the Sigmoid

A linear model predicts an unbounded value:

$$
z = mx + b, \qquad z \in (-\infty, \infty)
$$

But a probability must satisfy $p \in (0, 1)$, so $z$ cannot be used as $p$ directly.
The fix is to make the **log-odds** linear in $x$ instead of the probability itself:

$$
\log\left( \frac{p}{1 - p} \right) = mx + b
$$

The quantity $\frac{p}{1-p}$ is the **odds**, and its logarithm is the **logit**, which maps $(0,1) \to (-\infty, \infty)$ — exactly the range of $z$.

**Solving for $p$.** Exponentiate both sides:

$$
\frac{p}{1 - p} = e^{mx + b}
$$

Multiply through by $(1 - p)$:

$$
p = (1 - p)\, e^{mx + b} = e^{mx + b} - p\, e^{mx + b}
$$

Collect the $p$ terms:

$$
p + p\, e^{mx + b} = e^{mx + b}
\quad \Longrightarrow \quad
p \left( 1 + e^{mx + b} \right) = e^{mx + b}
$$

$$
p = \frac{e^{mx + b}}{1 + e^{mx + b}}
$$

Divide numerator and denominator by $e^{mx + b}$:

$$
p = \frac{1}{1 + e^{-(mx + b)}} = \sigma(mx + b)
$$

### Sigmoid Function

$$
\sigma(z) = \frac{1}{1 + e^{-z}}, \qquad \sigma(z) \in (0, 1)
$$

Its derivative has a convenient closed form:

$$
\sigma'(z) = \sigma(z)\left(1 - \sigma(z)\right)
$$

### Classification

In vector form for $d$ features, $z = \mathbf{w}^\top \mathbf{x} + b$ and

$$
P(y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w}^\top \mathbf{x} + b),
\qquad
P(y = 0 \mid \mathbf{x}) = 1 - \sigma(\mathbf{w}^\top \mathbf{x} + b)
$$

Predict class 1 when $p \geq 0.5$, which is equivalent to $z \geq 0$ — so the decision boundary $\mathbf{w}^\top \mathbf{x} + b = 0$ is a hyperplane.


