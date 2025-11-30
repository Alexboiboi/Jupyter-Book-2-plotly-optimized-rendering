---
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Multiple Plotly Plots - PNG + HTML Rendering

This page tests how Jupyter Book handles many **complex Plotly plots** with PNG rendering for fast loading and interactive features on hover.

## Performance Notes

With the `plotly_mimetype+png` renderer and **large datasets**:

- Static PNG images load immediately
- Interactive features activate only when hovering/clicking
- This reduces initial page load time and memory usage
- Only the actively viewed plot needs full interactive rendering
- **Data Volume**: Each plot contains 4,000-20,000+ data points
- **Complexity**: Subplots, WebGL acceleration, multiple traces
- Scroll through the page to test performance!

## Setup

```{code-cell} python
:tags: [hide-input]

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.io as pio
from plot_generator import generate_plots

# Configure Plotly to output both static and interactive formats
pio.renderers.default = "plotly_mimetype+png"

# Set random seed for reproducibility
np.random.seed(42)
```

## Generate Plots

```{code-cell} python
:tags: [hide-input]

# Generate plots (uses PLOT_COUNT env var, defaults to 2 locally, 50 in CI)
generate_plots()
```
