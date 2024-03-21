# Take-Home Exercise Overview
## Objective:
Implement a Python application that pulls data from a public API, stores it in a SQLite database, and incorporates database migration for schema evolution. The project should use Poetry for dependency management and enforce code quality through pre-commit hooks.

## Duration: 4-6 hours.

## Requirements
* **Language**: Python (Version 3.8+ recommended).
* **Database**: SQLite.
* **Source Control**: GitHub.
* **Dependency Management**: Poetry.
* **Data Source**: Any public API of your choice (e.g., a weather API, public data API like OpenWeatherMap, or GitHub API).

## Setup Instructions
1. **Fork and Clone Repository**: Provide a starter GitHub repository with minimal setup including a `pyproject.toml` for Poetry and a README with these instructions.
2. **Poetry Setup**:
  * Candidates should install Poetry on their local system.
  * Use Poetry to manage project dependencies. Include dependencies such as requests for API calls, `sqlalchemy` for database interaction, and `alembic` for database migrations, alongside `black` for formatting and `flake8` for linting.
3. **Pre-commit Hooks**:
  * Set up pre-commit hooks using the `pre-commit` package.
  * Configure hooks for `black`, `flake8`, and ensure Poetry's lock file is up to date.

## Task Description
1. **API Data Retrieval**:
  * Choose a public API and document how to register and get an API key if necessary.
  * Implement a script to pull data from the API using the `requests` library.
2. **Data Storage**:
  * Define a database schema in SQLite suitable for the data retrieved from the API.
  * Store the retrieved data in the database using `sqlalchemy`.
3. **Database Migration**:
  * Given the evolving nature of data, demonstrate a schema migration using `alembic`.
  * For example, add a new column to store additional data from the API or change a column type.

## Submission Instructions
* Commit and push all code to your forked repository on GitHub.
* Include clear documentation in the README for:
  * How to install and run the application.
  * A brief description of the application architecture and how it works.
  * Instructions for executing the database migration.
* Ensure the project follows Python's PEP 8 style guide, leveraging pre-commit hooks for enforcement.

## Evaluation Criteria
* **Functionality**: The application accurately retrieves data from the public API and stores it in the database.
* **Code Quality**: Clean, modular, and well-documented code. Proper use of Poetry for dependency management and adherence to PEP 8 through pre-commit hooks.
* **Documentation**: Clear setup and execution instructions, along with a good explanation of the application's architecture.
* **Error Handling and Logging**: Proper handling of errors and exceptions, with informative logging for troubleshooting.
* **Use of Git**: Effective use of git for version control, including meaningful commit messages.
