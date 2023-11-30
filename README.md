
# Project Name

This project encompasses Locust load tests and a Node.js mock server designed to simulate API endpoints for testing purposes.

## Node.js Mock Server

The Node.js mock server mimics specific API endpoints, such as `/login` and `/register`, and is ideal for local testing in conjunction with the Locust scripts.

### Prerequisites

- Node.js
- npm (Node Package Manager)

Download and install Node.js and npm from [here](https://nodejs.org/).

### Setup

1. **Navigate to the Node.js Server Directory:**

   ```sh
   cd node-mock-server
   ```

2. **Install Dependencies:**

   ```sh
   npm install
   ```

### Running the Server

Run the server in the `node-mock-server` directory:

```sh
node server.js
```

The server will be available at `http://localhost:3000`.

### Endpoints

- `POST /login`: Returns a fake JWT token.
- `POST /register`: Returns a mock UserDto object.

## Locust Load Testing

The Locust load tests are designed to simulate user traffic and measure the performance of the API endpoints.

### Prerequisites

- Python
- Locust

Install Python from [here](https://www.python.org/downloads/). Then install Locust using pip:

```sh
pip install locust
```

### Setup

1. **Navigate to the Locust Tests Directory:**

   ```sh
   cd locust-tests
   ```

2. **Install Python Dependencies:**

   If there's a `requirements.txt`, install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

### Running the Load Tests

1. **Start the Locust Interface:**

   In the `locust-tests` directory, run:

   ```sh
   locust
   ```

2. **Access the Web Interface:**

   Open a web browser and go to `http://localhost:8089`.

3. **Configure and Run the Tests:**

   - Enter the desired number of users and spawn rate.
   - Set the host to the mock server (`http://localhost:3000`).
   - Start the test and observe the results.

### Test Configuration

- Modify the `locustfile.py` and other scripts in the `tasks/` directory to define user behavior and tasks.
- Adjust configurations in the `config/` directory as needed.

## Notes

- The Node.js server is for testing only and not for production use.
- Update the mock server code (`server.js`) to align with your actual API behavior.

## Contributing

Contributions are welcome. Submit pull requests or suggest improvements via issues.

---

Contact the project maintainers for additional information or support.
