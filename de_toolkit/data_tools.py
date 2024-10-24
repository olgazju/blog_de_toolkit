import os

import pandas as pd
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(override=True)


def get_database_url() -> str:
    """
    Retrieve the database URL from environment variables.

    Returns:
        str: The database URL stored in the environment variable `DATABASE_URL`.
    """
    return os.getenv("DATABASE_URL")


def get_api_key() -> str:
    """
    Retrieve the API key from environment variables.

    Returns:
        str: The API key stored in the environment variable `API_KEY`.
    """
    return os.getenv("API_KEY")


def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file and clean it by removing duplicates and NaN values.

    Args:
        file_path (str): The path to the CSV file to be loaded.

    Returns:
        pd.DataFrame: A cleaned DataFrame with duplicates and NaN values removed.
    """
    data = pd.read_csv(file_path)
    cleaned_data = data.dropna().drop_duplicates()
    return cleaned_data


def main():
    """Entry point for the CLI."""
    # Print sensitive information (for demo purposes only – avoid in production!)
    print(f"Database URL: {get_database_url()}")
    print(f"API Key: {get_api_key()}")

    # Load and print the first few rows of the CSV
    df = load_and_clean_data("sample_data.csv")
    print("Cleaned Data:")
    print(df.head())


if __name__ == "__main__":
    main()
