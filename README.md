# Karl Pearson's Correlation Coefficient Calculator

## Introduction

Karl Pearson's Correlation Coefficient is a measure of the strength and direction of the linear relationship between two variables. It is suitable for continuous data and assumes that both variables are normally distributed. The coefficient $r$ ranges from -1 to 1, where:
- $r = 1$: Perfect positive correlation.
- $r = -1$: Perfect negative correlation.
- $r = 0$: No correlation.

## Methods

### 1. Direct Method
**Use When:** Input values are small.

**Formula:**
$$
\text{cov}(x, y) = \left(\frac{\Sigma(xy)}{n}\right) - (\bar{x} \cdot \bar{y})
$$

$$
\sigma_x = \sqrt{\frac{\Sigma(x^2)}{n}}
$$

$$
\sigma_y = \sqrt{\frac{\Sigma(y^2)}{n}}
$$


### 2. Deviation from Mean Method
**Use When:** Input values may vary.

**Formula:**
$$
\text{cov}(x, y) = \frac{\Sigma(x - \bar{x})(y - \bar{y})}{n}
$$

$$
\sigma_x = \sqrt{\frac{\Sigma(x - \bar{x})^2}{n}}
$$

$$
\sigma_y = \sqrt{\frac{\Sigma(y - \bar{y})^2}{n}}
$$


### 3. Assumed Mean Method
**Use When:** Mean values are floating point numbers.

**Formula:**
$$
\text{cov}(x, y) = \left(\frac{\Sigma(dx \cdot dy)}{n}\right) - \left(\frac{\Sigma(dx)}{n} \cdot \frac{\Sigma(dy)}{n}\right)
$$

$$
\sigma_x = \sqrt{\left(\frac{\Sigma(dx^2)}{n}\right) - \left(\frac{\Sigma(dx)}{n}\right)^2}
$$

$$
\sigma_y = \sqrt{\left(\frac{\Sigma(dy^2)}{n}\right) - \left(\frac{\Sigma(dy)}{n}\right)^2}
$$

## Usage

### Beginner Installation

1. Install the requirements (only once):
   ```bash
   pip install -r requirements.txt
   ```
2. Run the program:
   ```bash
   python karl_pearson.py
   ```

### Advanced Installation (Recommended for Future Runs)

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On MacOS/Linux
   venv\Scripts\activate       # On Windows
   ```
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program as desired:
   ```bash
   python karl_pearson.py
   ```
   *Deactivate the environment* after use with `deactivate`.

### Sample Input and Output

The program takes two lists of integers as input for $x$ and $y$, and computes the correlation coefficient using the chosen method based on the input characteristics.