var page = require('webpage').create();
page.open('http://localhost:5000/badge/Some random motherfucker/Participant/', function() {
  page.render('iot-weekend-countdown.png');
  phantom.exit();
});
