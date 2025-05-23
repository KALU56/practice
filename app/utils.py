import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load CSV data from a given file path."""
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def plot_boxplot(data, metric):
    """Return a boxplot figure for the given metric."""
    fig, ax = plt.subplots()
    sns.boxplot(y=metric, data=data, ax=ax)
    ax.set_title(f"{metric} Distribution")
    return fig

def get_top_regions(data, metric, top_n=10):
    """Return a dataframe of top N regions by average metric value."""
    return (
        data.groupby("Region")[metric]
        .mean()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )
