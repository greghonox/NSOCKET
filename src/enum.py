from enum import Enum


class Server(Enum):
    port = 8000
    ip = '127.0.0.1'
    len_buffer = 1024
    timeout = 60 * 2
    format_time = '%(asctime)s --- %(name)s --- %(threadName)s ---: %(message)s'
    is_live = True