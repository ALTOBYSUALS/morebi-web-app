#!/usr/bin/env node
/**
 * Simple HTTP server to serve the Webflow static website locally
 */
const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = 8000;

// MIME types for different file extensions
const mimeTypes = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'text/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.avif': 'image/avif',
  '.ico': 'image/x-icon',
  '.webp': 'image/webp'
};

function getMimeType(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  return mimeTypes[ext] || 'text/plain';
}

function serveFile(res, filePath) {
  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404, { 'Content-Type': 'text/html' });
      res.write('<h1>404 - Archivo no encontrado</h1>');
      res.end();
      return;
    }

    const mimeType = getMimeType(filePath);
    res.writeHead(200, { 
      'Content-Type': mimeType,
      'Access-Control-Allow-Origin': '*'
    });
    res.write(data);
    res.end();
  });
}

const server = http.createServer((req, res) => {
  let parsedUrl = url.parse(req.url);
  let pathname = parsedUrl.pathname;
  
  // Default to index.html for root path
  if (pathname === '/') {
    pathname = '/index.html';
  }
  
  const filePath = path.join(__dirname, pathname);
  
  // Check if file exists
  fs.access(filePath, fs.constants.F_OK, (err) => {
    if (err) {
      // Try to serve index.html for client-side routing
      serveFile(res, path.join(__dirname, 'index.html'));
    } else {
      serveFile(res, filePath);
    }
  });
});

server.listen(PORT, () => {
  console.log('🚀 Servidor iniciado en el puerto', PORT);
  console.log('📱 Abre tu navegador y ve a: http://localhost:' + PORT);
  console.log('🌐 También puedes usar: http://127.0.0.1:' + PORT);
  console.log('⏹️  Presiona Ctrl+C para detener el servidor');
  console.log();
});

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.log('❌ Error: El puerto', PORT, 'ya está en uso');
    console.log('💡 Intenta cerrar otros servidores o usa otro puerto');
  } else {
    console.log('❌ Error al iniciar el servidor:', err);
  }
});

process.on('SIGINT', () => {
  console.log('\n🛑 Servidor detenido');
  process.exit(0);
}); 