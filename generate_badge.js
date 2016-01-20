var page = require('webpage').create();
page.open('http://localhost:5000/badge/First Last/Participant/', function() {
  page.render('badge.png');
  phantom.exit();
});
