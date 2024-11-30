
# Trello Sprint Report Generator

This project automates the generation of sprint reports from Trello data. It leverages the power of AI agents to collect, analyze, and present key insights from your Trello boards, helping you keep your team and stakeholders informed about project progress, blockers, and potential delays.

## Features

* **Automated Data Collection:** Extracts relevant information from your Trello boards using the Trello Data Fetcher tool.
* **Intelligent Analysis:** Identifies potential blockers, delays, and assesses overall project progress.
* **Comprehensive Reporting:** Generates detailed sprint reports in markdown format, including:
    * Sprint overview
    * Task summary
    * Identified issues and blockers
    * Progress and delays
    * Team performance overview
    * Action items and recommendations

## Getting Started

### Prerequisites

* Python 3.9 or higher
* A Trello account with a project board

### Installation

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)


2.  **Create a virtual environment:**

    ```bash
    conda create -n trello-report-env python=3.9
    conda activate trello-report-env
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  **Trello API Key and Token:**

      - Obtain your Trello API key and token from the Trello Developer Portal.
      - Set these as environment variables or securely store them in a configuration file.

2.  **Trello Board ID:**

      - Get the ID of your Trello board.
      - Update the `data_collection_agent` in the `tasks.yaml` file with the correct board ID.

### Usage

1.  **Run the main script:**

    ```bash
    python main.py
    ```

2.  **View the report:**

      - The generated sprint report will be saved as a markdown file (e.g., `sprint_report.md`).
      - Open the file in any markdown viewer or editor.

