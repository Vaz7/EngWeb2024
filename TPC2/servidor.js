var http = require('http')
var fs = require('fs')
var url = require('url')

http.createServer(function (req, res){
    var regex = /^\/c([1-9][0-9]?|100)$/
    var q = url.parse(req.url, true)

    if(regex.test(q.pathname)){
        var filePath = 'html/' + q.pathname.substring(1) + '.html'
        
        // Check if file exists
        fs.access(filePath, fs.constants.F_OK, function(err) {
            if (err) {
                // Send 404 error if file does not exist
                res.writeHead(404, {'Content-Type': 'text/html; charset=utf-8'})
                res.end("<p>Erro 404: Página não encontrada.</p>")
            } else {
                // Read the file if it exists
                fs.readFile(filePath, function(err, data) {
                    if (err) {
                        res.writeHead(500, {'Content-Type': 'text/html; charset=utf-8'})
                        res.end("<p>Erro interno do servidor.</p>")
                    } else {
                        res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'})
                        res.write(data)
                        res.end()
                    }
                })
            }
        })
    } else if(q.pathname == '/w3.css'){
        fs.readFile('w3.css',function(err, data) {
            if (err) {
                res.writeHead(500, {'Content-Type': 'text/html; charset=utf-8'})
                res.end("<p>Erro interno do servidor.</p>")
            } else {
                res.writeHead(200, {'Content-Type': 'text/css'})
                res.write(data)
                res.end()
            }
        })
    } else if(q.pathname == '/my.css'){
        fs.readFile('my.css',function(err, data) {
            if (err) {
                res.writeHead(500, {'Content-Type': 'text/html; charset=utf-8'})
                res.end("<p>Erro interno do servidor.</p>")
            } else {
                res.writeHead(200, {'Content-Type': 'text/css'})
                res.write(data)
                res.end()
            }
        })
    } else if(q.pathname == '/favicon.ico'){
        fs.readFile('favicon.ico',function(err, data) {
            if (err) {
                res.writeHead(500, {'Content-Type': 'text/html; charset=utf-8'})
                res.end("<p>Erro interno do servidor.</p>")
            } else {
                res.writeHead(200, {'Content-Type': 'text/css'})
                res.write(data)
                res.end()
            }
        })
    }else if(q.pathname == '/'){
        fs.readFile('html/index.html',function(err, data) {
            if (err) {
                res.writeHead(500, {'Content-Type': 'text/html; charset=utf-8'})
                res.end("<p>Erro interno do servidor.</p>")
            } else {
                res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'})
                res.write(data)
                res.end()
            }
        })
    } else {
        res.writeHead(400, {'Content-Type': 'text/html; charset=utf-8'})
        res.write("<p>Erro: Pedido não suportado.</p>")
        res.write('<pre>' + q.pathname + '</pre>')
        res.end()
    }
    console.log(q.pathname)
}).listen(7777)
