<img src="https://img.shields.io/badge/python-v3.10.7-blue"/> <img src="https://img.shields.io/badge/mysql--connector--python-v8.0.30-blue"/> [![Dart](https://github.com/andre-moura/iot-hardware-simulator/actions/workflows/dart.yml/badge.svg?branch=main)](https://github.com/andre-moura/iot-hardware-simulator/actions/workflows/dart.yml)
# IoT Hardware Simulator
I created this project with the intention of simulating an IoT temperature sensor and sending its data to a MySQL database.

## Built using:

- Python
- MySQL

## How to get started

Clone the repository
```bash
git clone https://github.com/andre-moura/iot-hardware-simulator.git
```

 Install virtualenv at first
```bash
pip install virtualenv
```

Create virtual environments for our project.
```bash
virtualenv virtualenv_name
```

To activate a virtual environment, run the following command
```bash
source virtualenv_name/bin/activate
```

Download and install the libraries and dependencies
```bash
pip install requirements.txt
```

Run the application
```bash
python main.py
```
