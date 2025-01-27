import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data from a CSV file
def load_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    data = pd.read_csv(file_path)
    return data

# Function to display basic information about the dataset
def display_data_info(data):
    """
    Displays basic information about the dataset, such as columns, 
    number of rows, and missing values.
    
    Args:
        data (pd.DataFrame): Input dataset.
    """
    print("\n===== Dataset Info =====\n")
    print(data.info())  # Prints dataset structure
    print("\n===== Missing Values =====\n")
    print(data.isnull().sum())  # Summarizes missing values in the dataset

# Function to calculate descriptive statistics for specified columns
def calculate_statistics(data, columns):
    """
    Calculates mean, median, min, and max for specified columns in the dataset.
    
    Args:
        data (pd.DataFrame): Input dataset.
        columns (list): List of column names to compute statistics for.
        
    Returns:
        pd.DataFrame: DataFrame containing descriptive statistics.
    """
    stats = pd.DataFrame(columns=['Mean', 'Median', 'Min', 'Max'])
    for col in columns:
        stats.loc[col] = [
            data[col].mean(),
            data[col].median(),
            data[col].min(),
            data[col].max()
        ]
    return stats

# Function to visualize data distributions and box plots
def plot_all_graphs(data, stats_columns):
    """
    Plots histograms for data distributions and box plot for regional comparisons.
    
    Args:
        data (pd.DataFrame): Input dataset.
        stats_columns (list): Columns to visualize.
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    for i, col in enumerate(stats_columns):
        sns.histplot(data[col], kde=True, bins=10, ax=axes[i // 2, i % 2])
        axes[i // 2, i % 2].set_title(f"Distribution of {col}")
        axes[i // 2, i % 2].set_xlabel(col)
        axes[i // 2, i % 2].set_ylabel("Frequency")
    sns.boxplot(x="Region", y="Species_Population", data=data, ax=axes[1, 1])
    axes[1, 1].set_title("Species Population by Region")
    axes[1, 1].set_xlabel("Region")
    axes[1, 1].set_ylabel("Species Population")
    plt.tight_layout()
    plt.show()

# Function to visualize trends over time
def plot_trends(data):
    """
    Plots trends of species population across time using line plots.
    
    Args:
        data (pd.DataFrame): Input dataset with 'Timestamp' and 'Species_Population' columns.
    """
    plt.figure(figsize=(10, 6))
    for species in data['Species'].unique():
        species_data = data[data['Species'] == species]
        plt.plot(pd.to_datetime(species_data['Timestamp']), species_data['Species_Population'], label=species)
    plt.title("Species Population Trends Over Time")
    plt.xlabel("Time")
    plt.ylabel("Species Population")
    plt.legend()
    plt.show()

# Function to calculate and visualize correlation matrix
def calculate_correlation(data, columns):
    """
    Calculates and visualizes the correlation between specified columns.
    
    Args:
        data (pd.DataFrame): Input dataset.
        columns (list): Columns to calculate correlations for.
    """
    correlation_matrix = data[columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

# Main function to run the program
def main():
    """
    Main function to load the dataset, display information, compute statistics,
    and visualize trends, distributions, and correlations.
    """
    file_path = 'Tanvir_Arefin_Biostatistics_and_Ecological_Statistics_Visualization.csv'
    data = load_data(file_path)
    display_data_info(data)
    stats_columns = ['Temperature (\u00b0C)', 'Pollution_Level (ppm)', 'Species_Population']
    stats = calculate_statistics(data, stats_columns)
    print("\n===== Descriptive Statistics =====\n")
    print(stats.to_string())
    plot_all_graphs(data, stats_columns)
    plot_trends(data)
    calculate_correlation(data, stats_columns)

# Entry point of the script
if __name__ == "__main__":
    main()
