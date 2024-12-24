
# Individual Uppgift

## Project Overview
This project automates the transformation of data and its integration into a cloud-based workflow. It involves generating a CSV file, converting it to JSON, and deploying the results through a CI/CD pipeline on GitHub.

## Key Features
1. **Data Generation**: `generate.py` creates `profiles1.csv` by fetching data from an external system.
2. **Data Transformation**: `csvtojson.py` converts the generated CSV into JSON format.
3. **Cloud Automation**:
   - GitHub Actions triggers tests and ensures the pipeline runs smoothly on code changes.
   - Automatically verifies the data conversion process and deploys updated files.

## Workflow
1. **Data Pipeline**:
   - `generate.py` fetches and prepares the CSV data.
   - `csvtojson.py` transforms it into a structured JSON file.
2. **Continuous Integration/Continuous Deployment**:
   - Push changes to the repository to trigger GitHub Actions.
   - Tests are run to ensure code integrity and functionality.
   - Successful tests result in automatic deployment.

## Requirements
- Python 3+
- Pico CSS for frontend styling (used in `index.html`)
- GitHub Actions for pipeline management

## How to Use
1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Run `generate.py` to create `profiles1.csv`.
3. Convert the CSV file to JSON:
   ```bash
   python csvtojson.py
   ```
4. Push changes to GitHub to trigger the pipeline.

## File Details
- **`generate.py`**: Script for creating the initial CSV file.
- **`csvtojson.py`**: Converts CSV to JSON with validation.
- **`index.html`**: Displays JSON data on a styled webpage.
- **`.github/workflows/main.yml`**: Defines the GitHub Actions pipeline for testing and deployment.

## Testing and Deployment
Tests and deployments run automatically upon repository changes. Ensure that:
- The pipeline is green before merging.
- All transformations produce expected results.
