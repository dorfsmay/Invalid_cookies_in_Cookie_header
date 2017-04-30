var express = require('express');
var cookieParser = require('cookie-parser');
var app = express();

app.use(cookieParser());

app.get('/', function(req, resp) {
   console.log(req.cookies);
   resp.send('Got it!\n')
}) 

app.listen(8080, function () {
      console.log('Example app listening on port 8080!')
})

