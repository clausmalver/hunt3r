# Hunt3r
Hunt3r is a very small Python script tool that interacts with the Hunter.io API to perform domain search and email verification. It provides a convenient command-line interface to search for emails associated with a domain and to verify the validity of an email address.

## Features

- **Domain Search**: Retrieve email addresses associated with a given domain.
- **Email Verification**: Verify the validity of an email address.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/clausmalver/hunt3r.git
   ```

2. Navigate to the project directory:
   ```sh
   cd hunt3r
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Add your Hunter.io API key:
   ```sh
   echo "API_KEY=YOUR_HUNTER_API_KEY" > .env
   ```

Replace `"YOUR_HUNTER_API_KEY"` in the installation steps with your actual Hunter.io API key.

## Usage

### Domain Search

To search for emails associated with a domain, use the following command:
```sh
python hunt3r.py -d example.com
```

This will retrieve email addresses associated with the domain `example.com` and print them.

### Email Verification

To verify the validity of an email address, use the following command:
```sh
python hunt3r.py -e john@example.com
```

This will verify the email address `john@example.com` and print its status and result.

## Sources

- [Hunter.io API](https://hunter.io/api/v2/docs) - The script interacts with the Hunter.io API to perform domain search and email verification.
