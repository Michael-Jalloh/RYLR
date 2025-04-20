RYLR is a Python library for RYLR LoRa transceivers to simplifies communication with RYLR modules using Python. It provides an interface to send and receive LoRa messages, configure module parameters (e.g., frequency, spreading factor, and power settings), and manage network communication. The library abstracts the AT command interactions, making it easier to integrate LoRa connectivity into Python projects without dealing with low-level serial communication details.

Support for RYLR896 and RYLR406.

### Installation
```
pip install rylr
```

### Features

- Set and get device configuration (address, network ID, baudrate, etc.)
- Send and receive LoRa messages
- Built-in support for AES password hashing
- Simple AT command interface wrapper


### Usage
```python
from rylr import RYLR

# Initialize the module
modem = RYLR(port="/dev/ttyUSB0", addr="101", network="10")

# Set properties
modem.baudrate = 9600 
modem.band = "915000000" # 915 MHz
modem.password = "mypassword"

# Send data to address 102
modem.send("Hello", address=102)

# Receive data
print(modem.recv())

# Close the port when done
modem.close()
```

### Constructor
```python
RYLR(port="/dev/ttyUSB0", baud=115200, addr="100", network="10",  blocking=True, baudrate=None, band=None, mode=None, parameter=None, password=None, power=15)
```

### Properties

| Property    | Getter Method       | Setter Method                       | Description                  |
|-------------|---------------------|-------------------------------------|------------------------------|
| `address`   | `AT+ADDRESS?`       | `AT+ADDRESS=<addr>`                 | Device address (0–65535)     |
| `network`   | `AT+NETWORKID?`     | `AT+NETWORKID=<id>`                 | Network ID (0–16)            |
| `baudrate`  | `AT+IPR?`           | `AT+IPR=<rate>`                     | Baudrate (300–115200)        |
| `mode`      | `AT+MODE?`          | `AT+MODE=<mode>`                    | 0: Tx/Rx, 1: Sleep           |
| `band`      | `AT+BAND?`          | `AT+BAND=<freq>`                    | Frequency in Hz              |
| `parameter` | `AT+PARAMETER?`     | `AT+PARAMETER=<param>`              | LoRa parameters              |
| `password`  | `AT+CPIN`           | `AT+CPIN=<AES_MD5>`                 | AES password (MD5 hashed)    |
| `power`     | `AT+CRFOP?`         | `AT+CRFOP=<0–15>`                   | Transmission power (0–15 dBm)|
|


### Methods
- send(data, address=0): Send data to a specific LoRa address.

- recv(): Read incoming message (blocking).

- AT_command(command: str, wait_time: float=0.1): Send a raw AT command to the modem.

- close(): Closes the serial connection.

### Notes

    Make sure the correct serial port (/dev/ttyUSB0, COMx, etc.) is specified.

    This library assumes you're familiar with AT command configuration for the RYLR896/406 modules.