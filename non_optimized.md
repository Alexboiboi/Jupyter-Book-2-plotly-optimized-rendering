---
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Multiple Plotly Plots - HTML Rendering

This page tests how Jupyter Book handles many Plotly plots with normal HTML rendering.

## Performance Notes

With normal HTML rendering and many plots (compared to PNG fallback):

- **Build Process**: Slower - Full interactive HTML is generated during build
- **Rendering**: Faster - All plots are immediately interactive
- Full Plotly interactivity available from page load
- Higher initial page load time and memory usage
- All plots render interactively simultaneously
- Scroll through the page to test performance!

**Note**: Compare with the PNG fallback version for faster build times at the cost of slower interactive rendering.

## Setup

```{code-cell} python
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.io as pio

# Set random seed for reproducibility
np.random.seed(42)
```

## Generate Plots

```{code-cell} python
:tags: [hide-input]

# Different plot types to cycle through
plot_types = [
    'scatter', 'line', 'bar', 'histogram', 'box', 
    'heatmap', 'pie', 'violin', 'area', 'funnel'
]

for i in range(2):
    plot_type = plot_types[i % len(plot_types)]
    
    if plot_type == 'scatter':
        df = pd.DataFrame({
            'x': np.random.randn(50),
            'y': np.random.randn(50)
        })
        fig = px.scatter(df, x='x', y='y', title=f'Plot {i+1}: Scatter')
        
    elif plot_type == 'line':
        x = np.linspace(0, 10, 50)
        y = np.sin(x + i/10) + np.random.randn(50) * 0.1
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
        fig.update_layout(title=f'Plot {i+1}: Line Chart')
        
    elif plot_type == 'bar':
        categories = [f'Cat{j}' for j in range(5)]
        values = np.random.randint(10, 100, 5)
        fig = px.bar(x=categories, y=values, title=f'Plot {i+1}: Bar Chart')
        
    elif plot_type == 'histogram':
        data = np.random.normal(i/10, 1, 200)
        fig = px.histogram(x=data, nbins=20, title=f'Plot {i+1}: Histogram')
        
    elif plot_type == 'box':
        df = pd.DataFrame({
            'category': np.repeat(['A', 'B', 'C'], 20),
            'value': np.random.randn(60)
        })
        fig = px.box(df, x='category', y='value', title=f'Plot {i+1}: Box Plot')
        
    elif plot_type == 'heatmap':
        z = np.random.randn(10, 10)
        fig = go.Figure(data=go.Heatmap(z=z, colorscale='Viridis'))
        fig.update_layout(title=f'Plot {i+1}: Heatmap')
        
    elif plot_type == 'pie':
        labels = [f'Slice{j}' for j in range(4)]
        values = np.random.randint(10, 100, 4)
        fig = px.pie(values=values, names=labels, title=f'Plot {i+1}: Pie Chart')
        
    elif plot_type == 'violin':
        df = pd.DataFrame({
            'category': np.repeat(['X', 'Y', 'Z'], 30),
            'value': np.random.randn(90)
        })
        fig = px.violin(df, y='value', x='category', title=f'Plot {i+1}: Violin Plot')
        
    elif plot_type == 'area':
        x = np.linspace(0, 10, 50)
        y = np.cumsum(np.random.randn(50))
        fig = px.area(x=x, y=y, title=f'Plot {i+1}: Area Chart')
        
    elif plot_type == 'funnel':
        stages = ['Stage1', 'Stage2', 'Stage3', 'Stage4']
        values = [100, 75, 50, 25]
        fig = go.Figure(go.Funnel(y=stages, x=values))
        fig.update_layout(title=f'Plot {i+1}: Funnel Chart')
    
    # Show the plot
    fig.update_layout(height=400, width=600).show()
    
    # Add spacing between plots
    if (i + 1) % 10 == 0:
        print(f"\n--- {i+1} plots generated ---\n")
```
