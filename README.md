# Cookie Parser

A Python tool designed to analyze HTTP cookies from web server responses. This script extracts cookie attributes from `Set-Cookie` headers and saves the results in a JSON file for easy integration with web applications.

## Description

This project provides a simple yet powerful tool to parse and analyze cookies from HTTP responses. It is particularly useful for developers who need to inspect cookie attributes for security, compliance, or debugging purposes.

## Features

- **HTTP Request Handling**: Utilizes the `requests` library to send GET requests to specified URLs and retrieve server responses.
- **Cookie Analysis**: Parses `Set-Cookie` headers to extract cookie attributes, including `Secure`, `HttpOnly`, `SameSite`, and other custom attributes.
- **JSON Output**: Stores the analysis results in a structured JSON file, making it convenient for further processing and integration.
- **Error Handling**: Includes basic error handling to manage exceptions and ensure smooth execution.

## Installation

To use this tool, you need to have Python installed on your system. Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/cookie-parser.git
   cd cookie-parser
## Install Dependencies

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt