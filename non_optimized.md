---
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Multiple Plotly Plots - HTML Rendering

This page tests how Jupyter Book handles many **complex Plotly plots** with normal HTML rendering.

## Performance Notes

With normal HTML rendering and **large datasets** (compared to PNG fallback):

- **Build Process**: Slower - Full interactive HTML is generated during build
- **Rendering**: Faster - All plots are immediately interactive
- Full Plotly interactivity available from page load
- Higher initial page load time and memory usage
- All plots render interactively simultaneously
- **Data Volume**: Each plot contains 4,000-20,000+ data points
- **Complexity**: Subplots, WebGL acceleration, multiple traces

**Note**: Compare with the PNG fallback version for faster build times at the cost of slower interactive rendering.

## Setup

```{code-cell} python
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.io as pio
from plot_generator import generate_plots

# Set random seed for reproducibility
np.random.seed(42)
```

## Generate Plots

```{code-cell} python
:tags: [hide-input]

# Generate plots (uses PLOT_COUNT env var, defaults to 2 locally, 50 in CI)
generate_plots()
```
