Network Education Tool

**An educational Python project for learning networking, packet creation, and encryption through hands-on coding.**

This project was designed as a collaborative team project to demonstrate networking concepts, TCP packet handling, client-server communication, and packet visualization. It is intended as a **portfolio piece** for cyber security or networking-oriented applications.

---

Table of Contents

1. [Purpose](#purpose)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
4. [Training Path](#training-path)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Development Workflow](#development-workflow)
8. [Contributing](#contributing)
9. [License](#license)

---

Purpose

This project has multiple learning goals:

* Understand **TCP/IP packet structure** by creating custom packet objects.
* Learn **client-server communication** using Python sockets.
* Visualize packets in transit using a **slow-mode educational viewer**.
* Explore **packet injection** and network vulnerabilities in a controlled environment.
* Implement **encryption and decryption** layers to simulate secure communications.

This repo is suitable for team-based development, teaching new developers Python basics, and introducing networking concepts.

---

Project Structure

```
network-education-tool/
│
├── packet_generator/      # Create and validate TCP packet objects
├── client_server/         # Client-server socket communication
├── visualization_tool/    # Slow-mode packet viewer and log parser
├── injection_tool/        # Inject malformed packets and spoofing
├── encryption_layer/      # Encrypt/decrypt packets, key exchange
├── docs/                  # Architecture, API reference, and guides
└── tests/                 # Unit tests for all components
```

---

Getting Started

This project is structured as a **multi-stage learning path**:

1. **Training Sandbox:** Start with Python basics, data structures, and small exercises.
2. **Mini Network Exercises:** Practice creating TCP packets, sending/receiving data locally.
3. **Full Project Development:** Move to the main repo, integrate components, and implement visualization, injection, and encryption features.

For new developers, it’s recommended to work through the **training-sandbox repo** first before attempting the main project.

---

Installation

1. Clone the repository:

```bash
git clone https://github.com/chrismvelez97/network-education-tool.git
cd network-education-tool
```

2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

Usage

* **Packet Generator:**

```bash
python packet_generator/packet.py
```

Client/Server Testing

```bash
python client_server/server.py
python client_server/client.py
```

Visualization Tool

```bash
python visualization_tool/viewer.py
```

Encryption Layer

```bash
python encryption_layer/encrypt.py
python encryption_layer/decrypt.py
```

Each module includes **example scripts** and **documentation** in the `docs/` folder.

---

Development Workflow

* Use **feature branches**: `feature/<feature-name>`
* Submit **pull requests** to `develop`
* Conduct **code reviews** in `#code-reviews` (Discord)
* Log bugs in `#issues-bugs`
* Document all changes in `docs/`

Branching Model

```
main        # stable code only
develop     # integration branch
feature/*   # new features
hotfix/*    # urgent fixes
```

---

Contributing

* Read `CONTRIBUTING.md` for coding standards and PR workflow.
* Follow Python best practices and PEP8.
* Include **tests** with any new features.
* Keep commits small and descriptive.

---

License

This repository is licensed under the **MIT License**.
It covers **all code, guides, and documentation** in this repo, but does **not cover general networking or Python knowledge**, which is public domain.

See `LICENSE.md` for full details.

---

Optional Enhancements (Future)

* GitHub Actions for CI/CD testing
* EC2 deployment scripts for client-server experiments
* Expanded visualization with live packet animation
* Additional exercises for trainees in `training-sandbox`

---

I can also **create a companion README for your `training-sandbox` repo** next, which integrates exercises, mini-projects, and step-by-step Python lessons for your teammates.

Do you want me to do that now?
