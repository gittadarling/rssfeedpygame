# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import webbrowser

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Notitleidpsx</title>", "utf-8"))
        self.wfile.write(bytes('<style>', "utf-8"))
        self.wfile.write(bytes("        /* Add a black background color to the top navigation */", "utf-8"))
        self.wfile.write(bytes(".topnav {", "utf-8"))
        self.wfile.write(bytes("  background-color: #333;", "utf-8"))
        self.wfile.write(bytes("  overflow: hidden;", "utf-8"))
        self.wfile.write(bytes("}", "utf-8"))
        self.wfile.write(bytes("/* Style the links inside the navigation bar */", "utf-8"))
        self.wfile.write(bytes(".topnav a {", "utf-8"))
        self.wfile.write(bytes("  float: left;", "utf-8"))
        self.wfile.write(bytes("  color: #f2f2f2;", "utf-8"))
        self.wfile.write(bytes("  text-align: center;", "utf-8"))
        self.wfile.write(bytes("  padding: 14px 16px;", "utf-8"))
        self.wfile.write(bytes("  text-decoration: none;", "utf-8"))
        self.wfile.write(bytes("  font-size: 17px;", "utf-8"))
        self.wfile.write(bytes("}", "utf-8"))
        self.wfile.write(bytes("/* Change the color of links on hover */", "utf-8"))
        self.wfile.write(bytes(".topnav a:hover {", "utf-8"))
        self.wfile.write(bytes("  background-color: #ddd;", "utf-8"))
        self.wfile.write(bytes("  color: black;", "utf-8"))
        self.wfile.write(bytes("}", "utf-8"))
        self.wfile.write(bytes("/* Add a color to the active/current link */", "utf-8"))
        self.wfile.write(bytes(".topnav a.active {", "utf-8"))
        self.wfile.write(bytes(" background-color: #04AA6D;", "utf-8"))
        self.wfile.write(bytes("  color: white;", "utf-8"))
        self.wfile.write(bytes("}", "utf-8"))
        self.wfile.write(bytes('</style>', "utf-8"))
        self.wfile.write(bytes('</head><body style="background-color: #000000" text="#ffffff">', "utf-8")) 
        self.wfile.write(bytes('         <div class="topnav">', "utf-8"))
        self.wfile.write(bytes('  <a class="active" href="#home">Home</a>', "utf-8"))
        self.wfile.write(bytes('  <a href="#news">News</a>', "utf-8"))
        self.wfile.write(bytes('  <a href="#contact">Contact</a>', "utf-8"))
        self.wfile.write(bytes('  <a href="#about">About</a>', "utf-8"))
        self.wfile.write(bytes("<p>Request: %s This is an example web server.                             <a href='#login'>Sign Up / Sign In</a></p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</div>", "utf-8"))
        from rss_parser import Parser
        from requests import get
        self.wfile.write(bytes('<div id="psxhax">', "utf-8"))
        rss_url = "https://www.psxhax.com/articles/index.rss"
        xml = get(rss_url)
        parser = Parser(xml=xml.content, limit=None)
        feed = parser.parse()
        ita = 1
        feed2 = " "
        for item in feed.feed:
            feed2 = feed2 + "<br>" + item.title
        self.wfile.write(bytes("<p> %s </p>" % feed2, "utf-8" ))           
        self.wfile.write(bytes("</div>", "utf-8"))
        self.wfile.write(bytes('<div id="yts">', "utf-8"))
        rss_url = "https://yts.mx/rss"
        xml = get(rss_url)
        parser = Parser(xml=xml.content, limit=None)
        feed = parser.parse()
        ita = 1
        feed2 = " "
        for item in feed.feed:
            feed2 = feed2 + "<br>" + item.title
        self.wfile.write(bytes("<p> %s </p>" % feed2, "utf-8" ))
        self.wfile.write(bytes("</div>", "utf-8"))
        self.wfile.write(bytes('<div id="wololo">', "utf-8"))
        rss_url = "http://wololo.net/feed"
        xml = get(rss_url)
        parser = Parser(xml=xml.content, limit=None)
        feed = parser.parse()
        ita = 1
        feed2 = " "
        for item in feed.feed:
            feed2 = feed2 + "<br>" + item.title
        self.wfile.write(bytes("<p> %s </p>" % feed2, "utf-8" ))
        self.wfile.write(bytes("</div>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    webbrowser.open('http://localhost:8080')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


