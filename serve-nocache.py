#!/usr/bin/env python3
"""
Simple HTTP server WITHOUT caching to force reload of changes
"""
import http.server
import socketserver
import os
import time

PORT = 8000

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Force no caching
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Last-Modified', time.strftime('%a, %d %b %Y %H:%M:%S GMT'))
        super().end_headers()

def main():
    # Change to the directory containing the HTML files
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor SIN CACHÉ iniciado en puerto {PORT}")
        print(f"📱 Abre: http://localhost:{PORT}")
        print(f"🔄 Los cambios se mostrarán inmediatamente")
        print("⏹️  Presiona Ctrl+C para detener")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor detenido")

if __name__ == "__main__":
    main() 