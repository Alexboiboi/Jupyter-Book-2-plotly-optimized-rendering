---
title: Jupyter Book with Plotly Optimized Rendering
authors:
  - name: Alexandre Boisselet
html_meta:
  "description lang=en": "Jupyter Book with Plotly optimized rendering examples"
  "keywords": "jupyter-book, plotly, optimization, rendering"
  "property=og:locale": "en_US"
---

# Jupyter Book with Plotly Optimized Rendering

This Jupyter Book demonstrates different approaches to rendering Plotly charts in Jupyter Book, comparing performance and user experience.

## Contents

- **[Non-Optimized Rendering](non_optimized.md)**: Traditional HTML rendering of Plotly plots
- **[Optimized Rendering](optimized.md)**: PNG fallback with interactive hover features

## Overview

Plotly charts can be rendered in multiple ways within Jupyter Book:

1. **Full HTML Rendering**: All plots are immediately interactive but can slow page load
2. **PNG + Interactive Fallback**: Static PNG images load fast, interactivity activates on hover

The optimized approach provides better performance for pages with many plots while maintaining the interactive experience when needed.

## Getting Started

To build this book locally:

```bash
pip install -e .
jupyter-book build --html --execute
```

### Full Build (Production)

```bash
PLOT_COUNT=20 jupyter-book build --html --execute
```

## Performance Comparison

| Method | Initial Load | Interactivity | Build Time | Data Volume |
|--------|-------------|---------------|------------|-------------|
| HTML Only | Slower | Immediate | Faster | High (50K+ points per plot) |
| PNG + HTML | Faster | On Hover | Slower | High (50K+ points per plot) |

**Key Improvements:**

- **Scatter plots** use WebGL acceleration (`scattergl`) with 50,000+ points (50 traces) in 2×2 subplots
- **Subplots** (2×2 grids) for scatter, line, and bar charts
- **Large datasets**: 4,000-10,000+ data points per visualization
- **Complex interactions**: Multiple overlaid traces and detailed hover information
