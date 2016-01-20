# Event printer

Flask app that generates a conference badge for participants, using PhantomJS and the ql570 library for printing with Brother QL range thermal printers.

### Running
```python
python routes.py
phantomjs generate_badge.js
```

### Setup
```bash
# event printer
git clone https://github.com/sasha42/Event-printer.git
pip install flask

# phantomjs
git clone https://github.com/spfaffly/phantomjs-linux-armv6l.git
tar -zxvf phantomjs-linux-armv6l/*.tar.gz
mv phantomjs-2.0.1-development-linux-armv6l/bin/phantomjs ~/Event-printer/.
```