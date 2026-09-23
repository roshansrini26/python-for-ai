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
