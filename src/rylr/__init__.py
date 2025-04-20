from serial import Serial
from hashlib import md5
from time import sleep

class RYLR(object):
    """
    RYLR896 and RYLR406
    """
    def __init__(self, port: str="/dev/ttyUSB0", baud: int=115200, addr: str="100", network: str="10", blocking=True,
                  baudrate: str = None, band: str = None, mode: str = None, parameter: str = None, password: str = None,
                  power: str = 15):
        self.port = Serial(port, baud, timeout=0.5)
        self.blocking = blocking
        if addr: self.address = addr
        if network: self.network = network
        if baudrate: self.baudrate = baudrate
        if band: self.band = band
        if mode: self.mode = mode
        if parameter: self.parameter = parameter
        if password: self.password = password
        if power: self.power = power
        
            
    @property
    def address(self):
        if self.blocking:
            self.AT_command("AT+ADDRESS?")
            sleep(0.1)
            return self.recv()
        return self.AT_command("AT+ADDRESS?")
    
    @address.setter
    def address(self, addr):
        """
        0~65535(default 0)
        """
        if self.blocking:
            self.AT_command(f"AT+ADDRESS={addr}")
            sleep(0.1)
            return self.recv()
        return self.AT_command(f"AT+ADDRESS={addr}")
    
    @property
    def network(self):
        if self.blocking:
            self.AT_command(f"AT+NETWORKID?")
            sleep(0.1)
            return self.recv()
        return self.AT_command("AT+NETWORKID?")
    
    @network.setter
    def network(self, network):
        """
        0~16(default 0)
        """
        if self.blocking:
            self.AT_command(f"AT+NETWORKID={network}")
            sleep(0.1)
            return self.recv()
        return self.AT_command(f"AT+NETWORKID={network}")
    
    @property
    def baudrate(self):
        if self.blocking:
            self.AT_command(f"AT+IPR?")
            sleep(0.1)
            return self.recv()
        return self.AT_command("AT+IPR?")

    @baudrate.setter
    def baudrate(self, baudrate):
        """
        300
        1200
        4800
        9600
        19200
        28800
        38400
        57600
        115200(default).
        """
        if self.blocking:
            self.AT_command(f"AT+IPR={baudrate}")
            sleep(0.1)
            return self.recv()
        return self.AT_command(f"AT+IPR={baudrate}")
    
    @property
    def mode(self):
        if self.blocking:
            self.AT_command(f"AT+MODE?")
            sleep(0.1)
            return self.recv()
        return self.AT_command("AT+MODE?")

    @mode.setter
    def mode(self, mode):
        """
        0:Transmit and Receive mode (default).
        1:Sleep mode.
        During the sleep mode, once the
        pin3(RX) receive any input data, the
        module will be woken up.
        """
        if self.blocking:
            self.AT_command(f"AT+MODE={mode}")
            sleep(0.1)
            return self.recv()
        return self.AT_command(f"AT+MODE={mode}")
    
    @property
    def band(self):
        if self.blocking:
            self.AT_command(f"AT+BAND?")
            sleep(0.1)
            return self.recv()
        return self.AT_command("AT+BAND?")
    
    @band.setter
    def band(self, band: str):
        """
        Frequency
        470000000: 470000000Hz(default: RYLR40x)
        915000000: 915000000Hz(default: RYLY89x)
        """
        if self.blocking:
            self.AT_command(f"AT+BAND={band}")
            sleep(0.1)
            return self.recv()
        return self.AT_command(f"AT+BAND={band}")

    @property
    def parameter(self):
        if self.blocking:
            self.AT_command(f"AT+PARAMETER?")
            sleep(0.1)
            return self.recv()
        return self.AT_command("AT+PARAMETER?")
    
    @parameter.setter
    def parameter(self, parameter: str):
        if self.blocking:
            self.AT_command(f"AT+PARAMETER={parameter}")
            sleep(0.1)
            return self.recv()
        return self.AT_command(f"AT+PARAMETER={parameter}")
    
    @property
    def password(self):
        if self.blocking:
            self.AT_command(f"AT+CPIN?")
            sleep(0.1)
            return self.recv()
        return self.AT_command("AT+CPIN?")
    
    @password.setter
    def password(self, password: str):
        """
        An 32 character long AES password
        From 00000000000000000000000000000001 to
        FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

        password is a string
        we use md5 to generate hexdegist
        """
        password_hexdigest = md5(password).hexdigest()
        if self.blocking:
            self.AT_command(f"AT+CPIN={password_hexdigest}")
            sleep(0.1)
            return self.recv()
        return self.AT_command(f"AT+CPIN={password_hexdigest}")
    
    @property
    def power(self):
        if self.blocking:
            self.AT_command(f"AT+CRFOP?")
            sleep(0.1)
            return self.recv()
        return self.AT_command("AT+CRFOP?")
    
    @power.setter
    def power(self, power:int = 15):
        """
        0~15
        15:15dBm(default)
        14:14dBm
        ……
        01:1dBm
        00:0dBm
        """
        if power > 15:
            power = 15
        elif power < 0:
            power = 0
        if self.blocking:
            self.AT_command(f"AT+CRFOP={power}")
            sleep(0.1)
            return self.recv()
        return self.AT_command(f"AT+CRFOP={power}")

    def send(self, data, address=0):
        msg_len = len(str(data))
        return self.AT_command(f"AT+SEND={address},{msg_len},{data}")
    
    def recv(self):
        try:
            if self.port.in_waiting:
                return self.port.readline().decode("utf-8")
        except Exception:
            pass
        return "null"
        
    def AT_command(self, command: str, wait_time: float=0.1):
        """
        format the cmd to an AT command"
        """
        command = command if command.endswith("\r\n") else command+ "\r\n"
        self.port.write(command.encode())
        return "OK"

    def close(self):
        self.port.close()        
