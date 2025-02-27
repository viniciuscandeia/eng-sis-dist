const http = require('http');

const hostname = '0.0.0.0'; // Escutar em todos os interfaces de rede
const port = 8080;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Olá Mundo! Você está acessando a aplicação DevOps.\n');
});

server.listen(port, hostname, () => {
    console.log(`Servidor rodando em http://<span class="math-inline">\{hostname\}\:</span>{port}/`);
});
