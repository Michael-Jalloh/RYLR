from serial import Serial
from hashlib import md5
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

class RYLR(object):
    """
    RYLR896 and RYLR406
    """
    def __init__(self, port: str="/dev/ttyUSB0", baudrate: int= 115200, addr: str="100", network: str="10", wait_time: float = 0.1,
                    band: str ="", mode: str ="", parameter: str ="", password: str ="",
                  power: str =""):
        self.port = Serial(port, baudrate, timeout=0.5)
        self.wait_time = wait_time
        if addr:
            self.address = addr
        if network: 
            self.network = network
        if band: 
            self.band = band
        if mode: 
            self.mode = mode
        if parameter: 
            self.parameter = parameter
        if password: 
            self.password = password
        if power: 
            self.power = power
        
            
    @property
    def address(self)-> str:
        if self.wait_time > 0:
            self.AT_command("AT+ADDRESS?")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command("AT+ADDRESS?")
    
    @address.setter
    def address(self, addr: str)-> str:
        """
        0~65535(default 0)
        """
        if self.wait_time > 0:
            self.AT_command(f"AT+ADDRESS={addr}")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command(f"AT+ADDRESS={addr}")
    
    @property
    def network(self)-> str:
        if self.wait_time > 0:
            self.AT_command("AT+NETWORKID?")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command("AT+NETWORKID?")
    
    @network.setter
    def network(self, network: str)-> str:
        """
        0~16(default 0)
        """
        if self.wait_time > 0:
            self.AT_command(f"AT+NETWORKID={network}")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command(f"AT+NETWORKID={network}")
    
    @property
    def baudrate(self)-> str:
        if self.wait_time > 0:
            self.AT_command("AT+IPR?")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command("AT+IPR?")

    @baudrate.setter
    def baudrate(self, baudrate: str)-> str:
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
        if self.wait_time > 0:
            self.AT_command(f"AT+IPR={baudrate}")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command(f"AT+IPR={baudrate}")
    
    @property
    def mode(self)-> str:
        if self.wait_time > 0:
            self.AT_command("AT+MODE?")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command("AT+MODE?")

    @mode.setter
    def mode(self, mode: str)-> str:
        """
        0:Transmit and Receive mode (default).
        1:Sleep mode.
        During the sleep mode, once the
        pin3(RX) receive any input data, the
        module will be woken up.
        """
        if self.wait_time > 0:
            self.AT_command(f"AT+MODE={mode}")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command(f"AT+MODE={mode}")
    
    @property
    def band(self)-> str:
        if self.wait_time > 0:
            self.AT_command("AT+BAND?")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command("AT+BAND?")
    
    @band.setter
    def band(self, band: str)-> str:
        """
        Frequency
        470000000: 470000000Hz(default: RYLR40x)
        915000000: 915000000Hz(default: RYLY89x)
        """
        if self.wait_time > 0:
            self.AT_command(f"AT+BAND={band}")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command(f"AT+BAND={band}")

    @property
    def parameter(self)-> str:
        if self.wait_time > 0:
            self.AT_command("AT+PARAMETER?")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command("AT+PARAMETER?")
    
    @parameter.setter
    def parameter(self, parameter: str)-> str:
        if self.wait_time > 0:
            self.AT_command(f"AT+PARAMETER={parameter}")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command(f"AT+PARAMETER={parameter}")
    
    @property
    def password(self)-> str:
        if self.wait_time > 0:
            self.AT_command("AT+CPIN?")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command("AT+CPIN?")
    
    @password.setter
    def password(self, password: str)-> str:
        """
        An 32 character long AES password
        From 00000000000000000000000000000001 to
        FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

        password is a string
        we use md5 to generate hexdegist
        """
        password_hexdigest = md5(password).hexdigest()
        if self.wait_time > 0:
            self.AT_command(f"AT+CPIN={password_hexdigest}")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command(f"AT+CPIN={password_hexdigest}")
    
    @property
    def power(self)-> str:
        if self.wait_time > 0:
            self.AT_command("AT+CRFOP?")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command("AT+CRFOP?")
    
    @power.setter
    def power(self, power: int = 15)-> str:
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
        if self.wait_time > 0:
            self.AT_command(f"AT+CRFOP={power}")
            sleep(self.wait_time)
            return self.recv()
        return self.AT_command(f"AT+CRFOP={power}")

    def send(self, data, address=0)-> str:
        msg_len = len(str(data))
        return self.AT_command(f"AT+SEND={address},{msg_len},{data}")
    
    def recv(self) -> str:
        try:
            if self.port.in_waiting:
                return self.port.readline().decode("utf-8")
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
        return "null"
        
    def AT_command(self, command: str) -> str:
        """
        format the cmd to an AT command"
        """
        command = command if command.endswith("\r\n") else command+ "\r\n"
        self.port.write(command.encode("utf-8"))
        return "OK"

    def close(self):
        self.port.close()
