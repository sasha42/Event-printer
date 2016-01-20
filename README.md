# Event printer

Flask app that generates a conference badge for participants, using PhantomJS and the ql570 library for printing with Brother QL range thermal printers.

### Running
```python
python routes.py
phantomjs generate_badge.js
```