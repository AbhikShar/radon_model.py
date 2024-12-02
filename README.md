# README: Analyzing the Relationship Between House Size and Radon Levels

## Overview
This project explores the relationship between house size (measured in square feet) and radon levels (measured in Bq/m³) using linear regression. It provides insights into whether a house's size could serve as a predictor for its radon levels, using a synthetic dataset for demonstration purposes.

## Prerequisites
Ensure you have the following Python libraries installed to run the code:

```bash
pip install numpy matplotlib scikit-learn
```

## Dataset
The dataset is synthetic and includes:

- **house_size**: A list of house sizes in square feet.
- **radon_level**: Corresponding radon levels in the houses.

### Example Data
```python
house_size = [1200, 1600, 2500, 1400, 1800, 2800, ...]
radon_level = [95, 45, 230, 110, 65, 320, ...]
