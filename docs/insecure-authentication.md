## Insecure Authentication Observations

Passwords are stored in plaintext inside a JSON file.
Anyone with access to the file can read and reuse credentials.

This demonstrates why plaintext storage must never be used in real systems.
