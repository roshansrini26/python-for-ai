# Linear Regression

## 1. What is Linear Regression?

Linear regression models the relationship between a **dependent variable** $y$ (target) and one or more **independent variables** $x$ (features) by fitting a straight line (or hyperplane).

The goal is to predict $y$ from $x$ and to understand how much $y$ changes when $x$ changes.

---

## 2. The Formula

The general model is:

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \varepsilon
$$

| Symbol | Meaning |
|---|---|
| $y$ | Actual value of the target |
| $\beta_0$ | Intercept (value of $y$ when all $x = 0$) |
| $\beta_1 \dots \beta_n$ | Coefficients (slope for each feature) |
| $x_1 \dots x_n$ | Input features |
| $\varepsilon$ | Error term (what the model cannot explain) |

The model's **prediction** drops the error term:

$$
\hat{y} = \beta_0 + \beta_1 x_1 + \dots + \beta_n x_n
$$

The error term $\varepsilon$ leads directly to the idea of residuals.

---

## 3. Residual Error

A **residual** is the difference between an actual value and the predicted value for one observation:

$$
e_i = y_i - \hat{y}_i
$$

- $e_i > 0$ → model **under-predicted**
- $e_i < 0$ → model **over-predicted**
- $e_i = 0$ → perfect prediction for that point

Summing raw residuals is useless (positives and negatives cancel), so we square them. The **Residual Sum of Squares (RSS)** is:

$$
RSS = \sum_{i=1}^{m} (y_i - \hat{y}_i)^2
$$

Minimising RSS is how we find the best line, but first the model must satisfy some assumptions.

---

## 4. Assumptions of Linear Regression

For the model's results to be reliable, the data should satisfy these assumptions (often remembered as **LINE** + no multicollinearity):

1. **Linearity**: the relationship between $x$ and $y$ is linear.
2. **Independence**: residuals are independent of each other (no autocorrelation, important for time-series data).
3. **Normality**: residuals are approximately normally distributed, $\varepsilon \sim N(0, \sigma^2)$.
4. **Equal variance (Homoscedasticity)**: residuals have constant variance across all values of $x$.
5. **No multicollinearity**: features are not strongly correlated with each other (applies to multiple regression).

**Quick checks:** residual vs. fitted plot (linearity, homoscedasticity), Q-Q plot (normality), Durbin-Watson test (independence), VIF (multicollinearity).

With the assumptions in place, we can find the line that fits best.

---

## 5. Line of Best Fit

The **line of best fit** is the line that minimises the RSS. This method is called **Ordinary Least Squares (OLS)**:

$$
\min_{\beta_0, \beta_1, \dots, \beta_n} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2
$$

Squaring the residuals:
- removes the sign so errors don't cancel out
- penalises large errors more than small ones
- gives a smooth function that can be minimised with calculus

How we solve OLS depends on how many features we have, which splits regression into two types.

---

## 6. Simple Linear Regression

One feature, one target:

$$
\hat{y} = \beta_0 + \beta_1 x
$$

Solving OLS gives closed-form coefficients:

$$
\beta_1 = \frac{\sum_{i=1}^{m} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{m} (x_i - \bar{x})^2} = \frac{\text{Cov}(x, y)}{\text{Var}(x)}
$$

$$
\beta_0 = \bar{y} - \beta_1 \bar{x}
$$

where $\bar{x}$ and $\bar{y}$ are the means. The fitted line always passes through the point $(\bar{x}, \bar{y})$.

**Example:** predicting house price from area alone.

---

## 7. Multiple Linear Regression

Two or more features:

$$
\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n
$$

In matrix form (with a column of 1s in $X$ for the intercept):

$$
\hat{\mathbf{y}} = X\boldsymbol{\beta}
$$

OLS solution (the **Normal Equation**):

$$
\boldsymbol{\beta} = (X^T X)^{-1} X^T \mathbf{y}
$$

**Interpretation:** $\beta_j$ is the change in $y$ for a one-unit increase in $x_j$, **holding all other features constant**.

**Example:** predicting house price from area, number of rooms, and location.

Once a model is fitted, we need numbers that tell us how good it is.

---

## 8. Evaluating a Linear Regression Model

All metrics below compare actual values $y_i$ with predictions $\hat{y}_i$ over $m$ observations.

### 8.1 Mean Absolute Error (MAE)

Average absolute size of the errors:

$$
MAE = \frac{1}{m} \sum_{i=1}^{m} |y_i - \hat{y}_i|
$$

- Same units as $y$, easy to interpret
- Treats all errors equally, so it's **robust to outliers**

### 8.2 Mean Squared Error (MSE)

Average of the squared errors:

$$
MSE = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2 = \frac{RSS}{m}
$$

- **Penalises large errors heavily**
- Units are squared ($y^2$), so it's harder to interpret directly
- Commonly used as the loss function during training

### 8.3 Root Mean Squared Error (RMSE)

Square root of MSE:

$$
RMSE = \sqrt{MSE} = \sqrt{\frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2}
$$

- Back in the **same units as $y$**
- Still penalises large errors more than MAE
- $RMSE \geq MAE$ always; a big gap between them signals some large errors (outliers)

### 8.4 Coefficient of Determination ($R^2$)

Proportion of the variance in $y$ explained by the model:

$$
R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

- $SS_{res}$ = RSS (unexplained variation)
- $SS_{tot}$ = total variation of $y$ around its mean

| $R^2$ value | Meaning |
|---|---|
| 1 | Perfect fit |
| 0 | No better than predicting the mean $\bar{y}$ |
| < 0 | Worse than predicting the mean |

**Adjusted $R^2$** (for multiple regression): plain $R^2$ never decreases when you add features, even useless ones. Adjusted $R^2$ penalises extra features:

$$
R^2_{adj} = 1 - \frac{(1 - R^2)(m - 1)}{m - n - 1}
$$

where $m$ = number of observations, $n$ = number of features.

---