# Invoicing Automation Cronjob

This repository hosts a Python script designed to automate the invoicing process with the Factureaza.ro platform.

## Functionality

The script performs the following tasks:

1. Retrieves a client ID based on the unique fiscal code (CIF).
2. Fetches the next invoice number in the series.
3. Increments the invoice number.
4. Creates a new invoice entry in XML format, detailing the services provided and their cost.
5. Submits the new invoice to Factureaza.ro.
6. Fetches the invoice PDF.
7. Emails the invoice as a PDF attachment to the accountant.
8. Updates an Excel template with relevant invoice information.
9. Emails the updated Excel file and the invoice to the employer.
10. Cleans up temporary files.

The script is designed to run as a cron job, automating the invoicing process on a schedule.

## Setup

The script uses a number of environment variables for configuration. For details, please see `config.py`.

## Usage

The script can be run directly:

```bash
python main.py
```

The application also comes with a Dockerfile for easy setup and deployment. This Dockerfile uses Python 3.11-slim as the base image and also installs LibreOffice, which is a requirement for some parts of the application. The Docker container is set to run the application upon startup.

To build and run the application using Docker:

```bash
docker build -t invoicing-automation-cronjob .
docker run invoicing-automation-cronjob
or using Docker:

```bash
docker build .
```

## Error Reporting

The script integrates with Sentry for error reporting. Make sure to set up the Sentry DSN in your environment.

## Dependencies

The script depends on several Python libraries, including `sentry_sdk` for error reporting, and utility modules for email and file handling. For a full list of dependencies, please see the imports at the beginning of `main.py`.
