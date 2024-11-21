const path = require('path');

// Serve static files from the 'scripts' folder
app.use('/scripts', express.static(path.join(__dirname, 'scripts')));
