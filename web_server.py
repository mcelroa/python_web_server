from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "192.168.1.148"
PORT = 9999

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello World</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>This is a POST</h1></body></html>", "utf-8"))

server = HTTPServer((HOST, PORT), MyServer)
print("Server Running...")
server.serve_forever()
server.server_close()
print("Server Closed.")