"""
Plot generator module for Jupyter Book Plotly examples.

This module contains shared functions for generating various types of Plotly plots
used in the non-optimized and optimized rendering examples.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

# Different plot types to cycle through
PLOT_TYPES = [
    "scatter",
    "line",
    "bar",
    "histogram",
    "box",
    "heatmap",
    "pie",
    "violin",
    "area",
    "funnel",
]


def get_plot_count() -> int:
    """
    Get the number of plots to generate from environment variable.

    Defaults to 4 for local development, can be overridden with PLOT_COUNT env var.

    Returns:
        Number of plots to generate
    """
    return int(os.getenv("PLOT_COUNT", "4"))


def generate_plot(plot_type: str, index: int) -> go.Figure:
    """
    Generate a single Plotly plot with substantial data for performance testing.

    Args:
        plot_type: Type of plot to generate
        index: Plot index for variation

    Returns:
        Plotly figure object with subplots and large datasets
    """
    # Create subplot layout based on plot type
    if plot_type in ["scatter", "line", "bar"]:
        # 2x2 subplot grid for these types
        from plotly.subplots import make_subplots

        fig = make_subplots(
            rows=2,
            cols=2,
            subplot_titles=[f"{plot_type.title()} {i + 1}" for i in range(4)],
            shared_xaxes=False,
            shared_yaxes=False,
        )
    else:
        # Single plot for other types
        fig = go.Figure()

    if plot_type == "scatter":
        # Generate large datasets with scattergl for WebGL acceleration
        for i in range(50):
            # 1000 points per trace (50,000 total points)
            n_points = 1000
            x = np.random.randn(n_points) + (i % 10) * 2  # 10 different x positions
            y = np.random.randn(n_points) + (i // 10) * 2  # 5 different y positions
            colors = np.random.randn(n_points)

            # Distribute across 4 subplots (roughly 12-13 traces per subplot)
            subplot_idx = i % 4
            row, col = (subplot_idx // 2) + 1, (subplot_idx % 2) + 1

            fig.add_trace(
                go.Scattergl(
                    x=x,
                    y=y,
                    mode="markers",
                    marker=dict(
                        size=2,  # Smaller points for more traces
                        color=colors,
                        colorscale="Viridis",
                        showscale=False
                    ),
                    name=f"Dataset {i + 1}",
                    showlegend=False,  # Too many legends would be messy
                ),
                row=row,
                col=col,
            )

        fig.update_layout(
            title=f"Plot {index + 1}: Scatter Plots (50 traces, 50,000 points total)",
            showlegend=False,
        )

    elif plot_type == "line":
        # Multiple high-density line plots
        for i in range(4):
            x = np.linspace(0, 10, 2000)  # 2000 points per line
            y = np.sin(x + i * np.pi / 4) * np.exp(-x / 10) + 0.1 * np.random.randn(
                2000
            )

            row, col = (i // 2) + 1, (i % 2) + 1
            fig.add_trace(
                go.Scatter(
                    x=x, y=y, mode="lines", name=f"Signal {i + 1}", line=dict(width=1.5)
                ),
                row=row,
                col=col,
            )

        fig.update_layout(
            title=f"Plot {index + 1}: Line Charts (8,000 points total)",
        )

    elif plot_type == "bar":
        # Multiple bar charts with many categories
        categories = [f"Cat_{j:03d}" for j in range(50)]  # 50 categories

        for i in range(4):
            values = np.random.exponential(10, 50) + i * 5  # Different distributions

            row, col = (i // 2) + 1, (i % 2) + 1
            fig.add_trace(
                go.Bar(x=categories, y=values, name=f"Group {i + 1}"), row=row, col=col
            )

        fig.update_layout(
            title=f"Plot {index + 1}: Bar Charts (200 bars total)", showlegend=False
        )

    elif plot_type == "histogram":
        # Multiple overlaid histograms with large datasets
        for i in range(3):
            # 2000 samples per distribution
            data = np.random.normal(i, 1, 2000)
            fig.add_trace(
                go.Histogram(
                    x=data, nbinsx=50, name=f"Distribution {i + 1}", opacity=0.7
                )
            )

        fig.update_layout(
            title=f"Plot {index + 1}: Histogram (6,000 samples)", barmode="overlay"
        )

    elif plot_type == "box":
        # Box plots with many categories and large samples
        categories = [f"Group_{j}" for j in range(20)]  # 20 categories
        all_data = []
        all_categories = []

        for cat in categories:
            # 200 samples per category
            data = np.random.normal(np.random.uniform(-2, 2), 1, 200)
            all_data.extend(data)
            all_categories.extend([cat] * len(data))

        df = pd.DataFrame({"category": all_categories, "value": all_data})
        fig = px.box(
            df,
            x="category",
            y="value",
            title=f"Plot {index + 1}: Box Plots (4,000 samples)",
        )

    elif plot_type == "heatmap":
        # Large heatmap
        z = np.random.randn(100, 100)  # 100x100 matrix
        fig.add_trace(go.Heatmap(z=z, colorscale="RdBu_r", showscale=True))
        fig.update_layout(
            title=f"Plot {index + 1}: Heatmap (10,000 cells)",
        )

    elif plot_type == "pie":
        # Pie chart with many slices
        labels = [f"Slice_{j:02d}" for j in range(25)]  # 25 slices
        values = np.random.exponential(10, 25)
        fig.add_trace(
            go.Pie(
                labels=labels,
                values=values,
                textinfo="none",  # Hide text for cleaner look
                hoverinfo="label+percent",
            )
        )
        fig.update_layout(
            title=f"Plot {index + 1}: Pie Chart (25 slices)",
        )

    elif plot_type == "violin":
        # Violin plots with large datasets
        categories = ["A", "B", "C", "D", "E"]  # 5 categories
        all_data = []
        all_categories = []

        for cat in categories:
            # 1000 samples per category
            data = np.random.normal(ord(cat) - ord("C"), 1, 1000)
            all_data.extend(data)
            all_categories.extend([cat] * len(data))

        df = pd.DataFrame({"category": all_categories, "value": all_data})
        fig = px.violin(
            df,
            y="value",
            x="category",
            title=f"Plot {index + 1}: Violin Plots (5,000 samples)",
        )

    elif plot_type == "area":
        # Stacked area chart with multiple series
        x = np.linspace(0, 10, 500)
        y_data = []
        for i in range(5):
            y = np.cumsum(np.random.randn(500)) + i * 10
            y_data.append(y)

        for i, y in enumerate(y_data):
            fig.add_trace(
                go.Scatter(
                    x=x,
                    y=y,
                    mode="lines",
                    fill="tonexty" if i > 0 else "tozeroy",
                    name=f"Series {i + 1}",
                )
            )

        fig.update_layout(
            title=f"Plot {index + 1}: Area Chart (2,500 points)",
        )

    elif plot_type == "funnel":
        # Funnel chart with many stages
        stages = [f"Stage_{j:02d}" for j in range(15)]  # 15 stages
        values = np.sort(np.random.exponential(100, 15))[::-1]  # Decreasing values
        fig.add_trace(go.Funnel(y=stages, x=values, textinfo="value+percent initial"))
        fig.update_layout(
            title=f"Plot {index + 1}: Funnel Chart (15 stages)",
        )

    else:
        raise ValueError(f"Unknown plot type: {plot_type}")

    return fig


def generate_plots(num_plots: int = None, show_progress: bool = True) -> None:
    """
    Generate and display multiple plots.

    Args:
        num_plots: Number of plots to generate (defaults to PLOT_COUNT env var, or 2)
        show_progress: Whether to show progress messages
    """
    if num_plots is None:
        num_plots = get_plot_count()

    for i in range(num_plots):
        plot_type = PLOT_TYPES[i % len(PLOT_TYPES)]
        fig = generate_plot(plot_type, i)

        # Show the plot
        fig.show()

        # Add spacing between plots
        if show_progress and (i + 1) % 10 == 0:
            print(f"\n--- {i + 1} plots generated ---\n")
