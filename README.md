# Minimalist Jupyter Book with Plotly

A simple Jupyter Book project demonstrating interactive Plotly visualizations with optimized rendering options.

## Quick Start

### Local Development (Fast)

By default, notebooks generate only 4 plots for quick testing:

```bash
pip install -e .
jupyter-book build --html --execute
```

### Full Build (Production)

Set `PLOT_COUNT=20` to generate all 20 plots:

```bash
PLOT_COUNT=20 jupyter-book build --html --execute
```

Or export the environment variable:

```bash
export PLOT_COUNT=20
jupyter-book build --html --execute
```

## GitHub Pages Deployment

The GitHub Actions workflow automatically sets `PLOT_COUNT=20` for full builds on deployment.

## Plot Complexity

Each plot now contains substantial data to demonstrate real performance differences:

- **Scatter plots**: 50,000+ points using WebGL-accelerated `scattergl` in 2×2 subplots (50 traces)
- **Line charts**: 8,000+ data points across multiple signals in 2×2 subplots  
- **Bar charts**: 200+ bars across multiple categories in 2×2 subplots
- **Histograms**: 6,000+ samples with overlaid distributions
- **Box plots**: 4,000+ samples across 20 categories
- **Heatmaps**: 10,000+ cells in 100×100 matrices
- **Pie charts**: 25 slices with detailed segmentation
- **Violin plots**: 5,000+ samples across 5 categories
- **Area charts**: 2,500+ points with stacked series
- **Funnel charts**: 15 stages with complex flows

## Rendering Options

- **Non-optimized**: Full HTML rendering (immediate interactivity, slower load)
- **Optimized**: PNG fallback with hover interactivity (faster load, interactive on demand)
