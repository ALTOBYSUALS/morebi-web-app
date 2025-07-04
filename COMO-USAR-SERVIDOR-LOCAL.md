# 🚀 Cómo Hacer Deploy Local de Tu Sitio Web

Este documento te explica cómo servir tu sitio web Webflow localmente en tu computadora.

## 📋 Requisitos

Tu sitio web es completamente estático (HTML, CSS, JavaScript, imágenes), así que solo necesitas uno de estos:

- **Python 3** (recomendado - suele estar preinstalado en Mac y Linux)
- **Node.js** (alternativa)
- **Navegador web** (Chrome, Firefox, Safari, etc.)

## 🔧 Opción 1: Usando Python (Recomendado)

### Paso 1: Verificar que tienes Python
Abre la terminal y ejecuta:
```bash
python3 --version
```

Si ves un número de versión (como `Python 3.9.7`), estás listo. Si no lo tienes, descárgalo desde [python.org](https://python.org).

### Paso 2: Ejecutar el servidor
En la terminal, navega hasta la carpeta de tu sitio web y ejecuta:
```bash
python3 serve.py
```

### Paso 3: Ver tu sitio web
Abre tu navegador y ve a:
- **http://localhost:8000** 
- **http://127.0.0.1:8000**

¡Listo! Tu sitio web debería estar funcionando.

## 🔧 Opción 2: Usando Node.js

### Paso 1: Verificar que tienes Node.js
```bash
node --version
```

Si no lo tienes, descárgalo desde [nodejs.org](https://nodejs.org).

### Paso 2: Ejecutar el servidor
```bash
node serve.js
```

### Paso 3: Ver tu sitio web
Ve a **http://localhost:8000** en tu navegador.

## 🔧 Opción 3: Método Rápido con Python (Una línea)

Si prefieres un comando más simple, también puedes usar:
```bash
python3 -m http.server 8000
```

## 🛠️ Solución de Problemas

### ❌ "Puerto ya en uso"
Si ves este error, significa que otro programa está usando el puerto 8000. Puedes:
1. Cerrar otros servidores
2. Usar otro puerto modificando el número en los scripts

### ❌ "Comando no encontrado"
- Para Python: Instala Python 3 desde [python.org](https://python.org)
- Para Node: Instala Node.js desde [nodejs.org](https://nodejs.org)

### ❌ Las fuentes o imágenes no se ven bien
Los scripts incluyen manejo de MIME types para archivos web comunes. Si tienes problemas, verifica que todos los archivos estén en las carpetas correctas:
- CSS en `css/`
- Imágenes en `images/`
- JavaScript en `js/`

## 📱 Acceso desde Otros Dispositivos

Si quieres ver tu sitio web desde otros dispositivos en tu red local:

1. Encuentra tu IP local:
   ```bash
   # En Mac/Linux
   ifconfig | grep "inet "
   
   # En Windows
   ipconfig
   ```

2. Usa esa IP en otros dispositivos:
   ```
   http://TU-IP-LOCAL:8000
   ```

## 🎯 Consejos Útiles

- **Actualizar cambios**: Si modificas archivos HTML/CSS/JS, solo recarga la página en el navegador
- **Detener servidor**: Presiona `Ctrl+C` en la terminal
- **Múltiples puertos**: Si necesitas múltiples servidores, cambia el puerto en los scripts
- **Desarrollo**: Estos scripts son perfectos para desarrollo local y testing

## 🌟 ¿Qué Viene Después?

Una vez que tu sitio web funcione localmente, puedes:
- Subir los archivos a un hosting web (Netlify, Vercel, GitHub Pages)
- Configurar un dominio personalizado
- Optimizar imágenes y archivos para producción

¡Disfruta tu sitio web local! 🎉 