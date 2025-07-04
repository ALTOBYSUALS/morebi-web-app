#!/usr/bin/env python3
"""
Simple HTTP server to serve the Webflow static website locally
"""
import http.server
import socketserver
import os
import sys
from pathlib import Path

def main():
    PORT = 8000
    
    # Change to the directory containing the HTML files
    os.chdir(Path(__file__).parent)
    
    # Custom handler to serve files with proper MIME types
    class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            # Prevent caching to ensure changes are always visible
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
        
        def guess_type(self, path):
            # Handle common web file types
            if path.endswith('.css'):
                return 'text/css'
            elif path.endswith('.js'):
                return 'text/javascript'
            elif path.endswith('.svg'):
                return 'image/svg+xml'
            elif path.endswith('.avif'):
                return 'image/avif'
            return super().guess_type(path)
    
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"🚀 Servidor iniciado en el puerto {PORT}")
            print(f"📱 Abre tu navegador y ve a: http://localhost:{PORT}")
            print(f"🌐 También puedes usar: http://127.0.0.1:{PORT}")
            print(f"⏹️  Presiona Ctrl+C para detener el servidor")
            print()
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Error: El puerto {PORT} ya está en uso")
            print(f"💡 Intenta cerrar otros servidores o usa otro puerto")
        else:
            print(f"❌ Error al iniciar el servidor: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 