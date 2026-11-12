
# Medical Device Update Simulator

A Python-based software engineering project that simulates medical device software update workflows, device operating states, safety alerts, and update validation.

The simulator was inspired by real-world troubleshooting challenges involving connected medical devices and software systems.

> **Disclaimer:** This is an independent educational simulation. It does not connect to, control, or update actual medical devices and is not intended for clinical use.

## Project Overview

Medical device software updates may require multiple conditions to be satisfied before an update can proceed.

For example:

- A device may need to stop an active operation before an update.
- Safety alerts may need to be acknowledged.
- The system must validate its current state before allowing an update.
- Conflicting requirements may prevent an update from proceeding.

This project provides a controlled environment for exploring these scenarios through a REST API and an interactive dashboard.

The goal is to demonstrate software engineering concepts such as:

- State management and transitions
- Business rule validation
- REST API development
- Database persistence
- Logging and troubleshooting
- Separation of concerns
- Error handling
- Software workflow simulation

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API backend |
| Streamlit | Interactive web dashboard |
| SQLite | Local database persistence |
| Requests | Communication between dashboard and API |
| Uvicorn | ASGI server for FastAPI |
| Git and GitHub | Version control and source code management |

## System Architecture

The application follows a layered architecture that separates user interaction, API communication, business logic, and data persistence.

```text
                 User
                   |
                   v
        +---------------------+
        | Streamlit Dashboard |
        |   streamlit_app.py  |
        +---------------------+
                   |
                   | HTTP Requests
                   v
        +---------------------+
        |    FastAPI Backend  |
        |        app.py       |
        +---------------------+
                   |
                   v
        +---------------------+
        |    Service Layer    |
        |      services/      |
        +---------------------+
                   |
                   v
        +---------------------+
        |    SQLite Database  |
        |      database.py    |
        +---------------------+

        Logging: logger.py
```

### Component Responsibilities

**Streamlit Dashboard**

Provides a visual interface for interacting with the simulated device and observing its current state.

**FastAPI Backend**

Exposes REST endpoints that receive requests from the dashboard and coordinate operations.

**Service Layer**

Contains application logic for validating simulated device operations, update prerequisites, and state transitions.

**SQLite Database**

Stores simulated device information and state data.

**Logging**

Records selected application events to support troubleshooting and workflow investigation.

## Repository Structure

```text
med-device-update-simulator/
|
|-- app.py
|-- database.py
|-- logger.py
|-- streamlit_app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|
|-- services/
|
|-- logs/
|
|-- .venv/                  # Local only; not committed
```

The `.venv` directory is created locally and should not be committed to GitHub.

## Implemented Features

### 1. Device State Management

The simulator provides controls for changing the simulated device's operating state.

Supported dashboard actions include:

- Stop Delivery
- Start Delivery
- Acknowledge Alert
- Start Update

### 2. Software Update Validation

The application evaluates simulated device conditions before allowing an update operation.

This demonstrates how business rules and safety prerequisites can affect software workflows.

### 3. REST API

FastAPI provides endpoints for interacting with the simulated device.

FastAPI also generates interactive API documentation for testing supported operations.

### 4. Interactive Dashboard

Streamlit provides a browser-based interface for viewing device state and triggering supported actions.

### 5. Database Persistence

SQLite supports local persistence of simulated device information.

### 6. Application Logging

The project includes logging functionality for selected application events.

**Current limitation:** Logging is not yet exposed as a complete event history or event counter in the Streamlit dashboard.

## Getting Started

Follow these instructions to run the simulator locally.

### Prerequisites

Install the following software:

- Python 3
- Git
- A terminal such as Git Bash, PowerShell, or the VS Code terminal

### Step 1: Clone the Repository

```bash
git clone https://github.com/githubb012/med-device-update-simulator.git
```

Navigate into the project directory:

```bash
cd med-device-update-simulator
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file contains the Python packages required for the project.

SQLite is included with Python and does not require a separate installation.

### Step 4: Start the FastAPI Backend

Open a terminal in the project directory with the virtual environment activated.

Run:

```bash
python -m uvicorn app:app --reload
```

The backend will normally start at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

Keep this terminal running.

### Step 5: Start the Streamlit Dashboard

Open a second terminal in the project directory.

Activate the virtual environment again.

For Windows Git Bash:

```bash
source .venv/Scripts/activate
```

Start the dashboard:

```bash
python -m streamlit run streamlit_app.py
```

Open the dashboard in your browser:

http://localhost:8501

Both the FastAPI backend and Streamlit dashboard must remain running for the full application workflow.

## Using the Simulator

Once the application is running:

1. Open the Streamlit dashboard.
2. Review the displayed simulated device state.
3. Select **Stop Delivery** to request a state change.
4. Observe the resulting state and alert information.
5. Select **Start Update** to test update validation.
6. Use **Acknowledge Alert** to acknowledge an active alert.
7. Repeat supported operations to explore different workflow conditions.

The simulator evaluates requests according to its implemented business rules.

Some operations may be rejected when required conditions have not been satisfied.

## Example Simulation Scenario

Consider a simulated medical device that must stop delivery before receiving a software update.

The workflow may involve:

1. A software update is requested.
2. The application checks whether delivery is stopped.
3. If delivery is active, the update is blocked.
4. Delivery is stopped.
5. The system evaluates any remaining alert-related prerequisites.
6. The update is attempted again.

This scenario illustrates how different software requirements interact during an update workflow.

The simulator is designed to explore these interactions without affecting real medical equipment.

## Troubleshooting

### Missing requirements.txt

If the dependency file is unavailable, the primary packages can be installed using:

```bash
python -m pip install fastapi "uvicorn[standard]" streamlit requests
```

A dependency file can then be generated:

```bash
python -m pip freeze > requirements.txt
```

### FastAPI Does Not Start

Confirm that:

- The virtual environment is activated.
- Dependencies are installed.
- The command is executed from the project root.
- Port 8000 is not already in use.

### Streamlit Dashboard Does Not Open

Confirm that Streamlit is installed:

```bash
python -m pip show streamlit
```

Restart the dashboard:

```bash
python -m streamlit run streamlit_app.py
```

### Dashboard Cannot Communicate With the Backend

Verify that FastAPI is running at:

http://127.0.0.1:8000

Both applications must be running simultaneously.

### Dashboard Alert Count or Logging Does Not Update as Expected

The dashboard's alert count and application event logging are separate concepts.

The existing dashboard does not provide a complete event counter or historical log viewer.

Alert display refresh behavior and event logging are areas identified for further improvement.

## Known Limitations

The current implementation has several limitations:

- The application is designed for local development.
- The simulator does not connect to actual medical devices.
- Dashboard event history is not yet implemented.
- Logging does not currently provide a complete dashboard event counter.
- Some dashboard state displays may require refresh improvements.
- Automated testing coverage has not yet been established.
- Containerization and CI/CD are planned improvements.

## Development Roadmap

### Sprint 1 — Initial Implementation

- [x] Create a Python-based simulation
- [x] Implement a FastAPI backend
- [x] Create a Streamlit dashboard
- [x] Add SQLite persistence
- [x] Implement simulated device operations
- [x] Add update validation logic
- [x] Add initial application logging
- [x] Use Git and GitHub for version control

### Sprint 2 — Testing and Reliability

- [ ] Investigate dashboard alert-count refresh behavior
- [ ] Implement a dashboard event counter
- [ ] Add an event history viewer
- [ ] Improve application logging
- [ ] Add automated unit tests with pytest
- [ ] Add API integration tests
- [ ] Improve error handling and validation
- [ ] Add Docker support
- [ ] Configure GitHub Actions for CI

### Future Improvements

- [ ] Expand simulated device scenarios
- [ ] Add additional update validation rules
- [ ] Improve workflow visualization
- [ ] Add more comprehensive test coverage
- [ ] Improve application documentation
- [ ] Explore deployment options

## Software Engineering Concepts Demonstrated

### Separation of Concerns

The application separates the user interface, API, business logic, and database operations into distinct components.

### State Management

Device operations depend on the current simulated state and the conditions required for a transition.

### Business Rule Validation

The application evaluates prerequisites before allowing selected operations.

### API Communication

The Streamlit dashboard communicates with FastAPI through HTTP requests.

### Persistence

SQLite allows simulated device state to be maintained through local database operations.

### Troubleshooting and Observability

Logging and state inspection support the investigation of simulated workflow behavior.

## Project Motivation

This project was inspired by troubleshooting challenges involving connected medical devices and software workflows.

In complex systems, individual requirements may appear reasonable but interact in unexpected ways.

Building the simulator provided an opportunity to explore these interactions while applying Python development, API design, database management, and software engineering principles.

The project is an independent educational implementation and does not reproduce proprietary medical device software.

## License

No license has been specified for this repository.

All rights are reserved unless a license is added.

## Repository

GitHub:

https://github.com/githubb012/med-device-update-simulator
