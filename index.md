---
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Minimalist Jupyter Book with Plotly

This is a simple example of a Jupyter Book featuring an interactive Plotly visualization.

## Interactive Visualization

Below is an example of a Plotly chart showing a simple scatter plot with a trend line.

```{code-cell} python
:label: plotly-scatter
import plotly.express as px
import pandas as pd

# Create sample data
data = {
    'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'y': [2.3, 4.1, 5.8, 7.2, 9.5, 11.1, 13.4, 15.2, 17.8, 19.5]
}
df = pd.DataFrame(data)

# Create an interactive scatter plot
fig = px.scatter(df, x='x', y='y', 
                 title='Interactive Plotly Scatter Plot',
                 labels={'x': 'X Values', 'y': 'Y Values'})

fig.update_traces(marker=dict(size=12, color='royalblue'))
fig.show()
```

## About This Book

This book demonstrates:
- MyST Markdown syntax with executable code cells
- Interactive Plotly visualizations
- Jupyter Book's ability to render dynamic content

Here we reference the plot above: [](#plotly-scatter)
