import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load CSV from local path."""
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        return pd.DataFrame()

def plot_boxplot(data, metric):
    """Generate a boxplot for a selected metric."""
    fig, ax = plt.subplots()
    sns.boxplot(y=metric, data=data, ax=ax)
    ax.set_title(f"{metric} Distribution")
    return fig

def get_top_regions(data, metric, top_n=10):
    """Return top regions by average metric value."""
    return (
        data.groupby("Region")[metric]
        .mean()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )
