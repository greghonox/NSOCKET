from socket import AF_INET, SOCK_STREAM, gethostbyname, SOL_SOCKET, SO_REUSEADDR, socket
from src.enum import Server
import logging


class NSocket:
    def __init__(self) -> None:
        logging.basicConfig(format=Server.format_time.value)
        self.logger = logger = logging.getLogger('ngrok')
        self.log('Init application', 1)

    def create(self) -> None:
        self.con = socket(AF_INET, SOCK_STREAM)
        self.con.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.con.settimeout(Server.timeout.value)
        self.con.bind((Server.ip.value, Server.port.value))
        self.con.listen()        
        self.log('Creating connection', 1)

    def run(self) -> None:
        count = 0
        while Server.is_live.value:
            try:
                self.con.listen()
                self.log(f'Aguardando conexao({count}) {Server.ip.value} {Server.port.value}', 1)
                dta, cli = self.con.accept()
                self.log(f'Recebido conexao {cli}')
                self.recv(dta)
                count += 1
            except KeyboardInterrupt as error: 
                self.log(f'Error: {error}', 2)
                break
            except TimeoutError as error:
                self.log(f'Error: {error}', 2)
            except Exception as error: 
                self.log(f'Error: {error}', 3)

    def recv(self, con) -> None:
        msg = con.recv(Server.len_buffer.value)
        self.log(msg.decode(), 1)
        con.close()
            
    def log(self, msg: str, types: int = 0) ->None:
        """
            return logs:
                0: info
                1: warning
                2: error
                3: exception
        """
        match types:
            case 0: 
                self.logger.info(msg)
            case 1: 
                self.logger.warning(msg)                
            case 2:
                self.logger.error(msg)                                
            case 3:
                self.logger.exception(msg)                        
                
    def __del__(self) -> None:
        self.log('close connection', 1)
        try: 
            self.con.close()
        except Exception as error: 
            self.log(f'Error: {error}', 3)