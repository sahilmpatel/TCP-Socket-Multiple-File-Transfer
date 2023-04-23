import socket
import ast
import os

HOST, PORT = "192.168.29.44", 9999


class ReceiveFiles:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.dest_fold = 'Receive Folder'
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def operation(self):
        with self.soc:
            self.soc.bind((self.host, self.port))
            self.soc.listen()
            print("started listening......")
            conn, addr = self.soc.accept()
            print(f"Connected by {addr}")
            self.file_operation(conn)

    def file_operation(self, conn):
        """
        Steps:
            1. Filename along with its size is received.
            2. buffer is initialised with file size. if it is >= 8192 bytes then chunk size
               of 8192 will be received else buffer as a chunk size will be received.
               Then it will be written to filename in the specified destination folder.
               The proces of receiving bytes of data continues till the size of the respective
               file bytes received.
        """
        with conn:
            filenames_sizes = conn.recv(1024)
            print(f"filenames received :{ast.literal_eval(filenames_sizes.decode('utf-8'))}")
            for filename, size in ast.literal_eval(filenames_sizes.decode('utf-8')):
                buffer = size
                with open(os.path.join(os.getcwd(), self.dest_fold, filename), 'wb') as f:
                    while buffer:
                        chunk_size = 8192 if buffer >= 8192 else buffer
                        data = conn.recv(chunk_size)
                        if not data:
                            break
                        f.write(data)
                        buffer -= len(data)
                    print(f"{filename}'s data received...")
            conn.send(b'file data transfer is done.')


receive_op = ReceiveFiles(HOST, PORT)
receive_op.operation()
