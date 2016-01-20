var page = require('webpage').create();
var system = require('system');
var address = "http://localhost:5000/print?id=" + system.args[1];
console.log(address)
page.open(address, function() {
  page.render('badge.png');
  phantom.exit();
});
