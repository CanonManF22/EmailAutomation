const WebHooks = require('node-webhooks');

const hook = new WebHooks({
  db: './webHookdDB.json',
  httpSuccessCodes: [200, 201, 202, 203, 204],
});

const emitter = hook.getEmitter();

emitter.on('*.success', function(shortname, statusCode, body) {
  console.log('Success on trigger webHook' + shortname + 'with status code', statusCode, 'and body', body);
});

emitter.on('*.failure', function(shortname, statusCode, body) {
  console.error('Error on trigger webHook' + shortname + 'with status code', statusCode, 'and body', body);
});

const express = require('express');

const app = express();

const port = process.env.PORT || 8080;
app.listen(port, () => console.log(`Server up and running on port ${port} !`));

app.get('/', (req, res) => {
  res.send(201);
  console.log('webhook hit');
});
