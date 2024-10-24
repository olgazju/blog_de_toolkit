# blog_de_toolkit

`blog_de_toolkit` is a Python toolkit designed to streamline common data engineering tasks, such as loading and cleaning CSV data, as well as securely managing environment variables using `.env` files. This project also includes pre-commit hooks to ensure code quality and a GitHub Actions workflow to automate testing and linting.

## Features
- **Load and clean data**: Remove duplicates and missing values from CSV files.
- **Environment management**: Securely handle credentials and API keys with `.env` files.
- **Pre-commit hooks**: Automated code formatting and linting with `black`, `flake8`, and `isort`.
- **CI/CD with GitHub Actions**: Automated testing and code quality checks on every push or pull request.

## Installation

To install the package after building it locally:

```bash
pip install dist/blog_de_toolkit-0.1.0-py3-none-any.whl

## Usage

### Python Usage Example

Here’s a quick example of how to use the library to load and clean data:

```python
from de_toolkit.data_tool import load_and_clean_data

df = load_and_clean_data("sample_data.csv")
print(df.head())

### Running the Tool from the Command Line

After installing the package, you can run the tool directly from the terminal to print the cleaned data and environment variables:

```bash
blog_de_toolkit

## Development Setup

Follow these steps to set up your development environment:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/blog_de_toolkit.git
   cd blog_de_toolkit


2. **Create and activate a virtual environment**:

    ```bash
    brew update && brew upgrade pyenv
    pyenv install 3.12.2
    pyenv virtualenv 3.12.2 de_toolkit
    pyenv local de_toolkit

    ```

3.  **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt

    ```

4. **Install and configure pre-commit hooks**:

    ```bash
    pip install pre-commit
    pre-commit install

    ```

5. **Run pre-commit hooks manually (optional)**:

    ```bash
    pre-commit run --all-files
    ```
