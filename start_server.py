#!/usr/bin/env python3
"""
Rose Day Surprise Website Server
A simple HTTP server to share your Rose Day surprise with your girlfriend!
"""

import http.server
import socketserver
import socket
import os
import sys

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        # Create a socket to find the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

def start_server(port=8000):
    """Start the HTTP server"""
    
    # Change to the directory containing the HTML file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create the server
    Handler = http.server.SimpleHTTPRequestHandler
    
    # Suppress logging for cleaner output (optional)
    class QuietHandler(Handler):
        def log_message(self, format, *args):
            pass  # Suppress default logging
    
    with socketserver.TCPServer(("", port), Handler) as httpd:
        local_ip = get_local_ip()
        
        print("=" * 60)
        print("🌹 Rose Day Surprise Server Started! 🌹")
        print("=" * 60)
        print(f"\n✨ Your website is now live!\n")
        print(f"📱 Share this link with your girlfriend:\n")
        print(f"   🔗 http://{local_ip}:{port}/rose_day_surprise.html")
        print(f"\n💡 Alternative (if on same network):")
        print(f"   🔗 http://localhost:{port}/rose_day_surprise.html")
        print(f"\n⚠️  Keep this terminal window open to keep the website running!")
        print(f"⏹️  Press Ctrl+C to stop the server when you're done.\n")
        print("=" * 60)
        print(f"Server is running on port {port}...")
        print("=" * 60 + "\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🌹 Server stopped. Happy Rose Day! 🌹\n")
            sys.exit(0)

if __name__ == "__main__":
    # You can change the port number if needed
    PORT = 8000
    
    # Check if rose_day_surprise.html exists
    if not os.path.exists("rose_day_surprise.html"):
        print("❌ Error: rose_day_surprise.html not found!")
        print("Make sure this script is in the same folder as the HTML file.")
        sys.exit(1)
    
    start_server(PORT)
