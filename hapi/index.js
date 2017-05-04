'use strict';
const Hapi = require('hapi');
const server = new Hapi.Server();

server.connection({ port: 3000, host: 'localhost' });

server.route({
  method: 'GET',
  path: '/',
  handler: (request, reply) => {
    console.log('Cookie: ' + JSON.stringify(request.state) );
    return reply('Success');
  }
});

server.start( err => {
  if (err) { throw err; }
  console.log(`Server running at: ${server.info.uri}`);
});
