const http = require('http');
const fs = require('fs');
const { exec } = require('child_process');

const server = http.createServer((req, res) => {
  if (req.url === '/run-python') {
    exec('python app.py', (error, stdout, stderr) => {
      if (error) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(`Error: ${error.message}`);
        return;
      }

      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end(`stdout: ${stdout}\n\nstderr: ${stderr}`);
    });
  } else {
    fs.readFile('index.html', (err, data) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(`Error: ${err}`);
        return;
      }

      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(data);
    });
  }
});

server.listen(8080, () => {
  console.log('Server started on port 8080');
});
