# TCP-Socket-Multiple-File-Transfer


Steps of the communication:
  1. The connection is established via three-way handshake between the server and client.
  2. The Client sends filename along with its size.
  3. The Server receives filename with size.
     - size is necessary to set buffer to accept the chunks of bytes.
     - so there is no another measure to distinguish among the files data bytes and one file data will be appened to another file.
     - to avoid such case the size of the file is used to differentiate files.  
  4. The Client sends the file streams via sendfile() method until EOF is reached.
  5. The Server receives the chunks of bytes until the respective file size bytes received.
  
