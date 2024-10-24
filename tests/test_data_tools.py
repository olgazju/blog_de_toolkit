from io import StringIO

from de_toolkit.data_tools import get_database_url, get_api_key, load_and_clean_data


def test_load_and_clean_data():
    """Test that load_and_clean_data removes NaNs and duplicates."""
    csv_data = """name,age,city
    Alice,30,New York
    Bob,25,Los Angeles
    Alice,30,New York
    Charlie,,San Francisco
    Eve,29,Chicago
    Eve,29,Chicago"""

    data = StringIO(csv_data)  # Simulates a CSV file
    df = load_and_clean_data(data)

    # Check if duplicates and NaNs were removed correctly
    assert df.shape == (3, 3)
    assert not df.isna().any().any()
    assert df["name"].nunique() == 3


def test_get_database_url(monkeypatch):
    """Test that get_database_url retrieves the correct value."""
    monkeypatch.setenv("DATABASE_URL", "url")
    assert get_database_url() == "url"


def test_get_api_key(monkeypatch):
    """Test that get_api_key retrieves the correct value."""
    monkeypatch.setenv("API_KEY", "123456789abcdef")
    assert get_api_key() == "123456789abcdef"
