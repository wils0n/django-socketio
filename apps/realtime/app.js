var restify = require('restify');

var server = restify.createServer();
var io = require('socket.io').listen(server);

io.on('connection', function(socket){
    console.log('a user connect');
	socket.on('message', function(msg){
		console.log(msg);
        socket.broadcast.emit('message', msg);
	});
});

server.listen(3000, function() {
  console.log('%s listening at %s', server.name, server.url);
});
