from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello from Python Docker Web Server! Task 4.2 Credit</h1></body></html>")

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8080), SimpleHTTP)
    print("Server running on port 8080...")
    server.serve_forever()