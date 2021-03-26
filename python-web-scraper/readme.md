#Web Scraper
## Useage
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python scraper.py -d https://scrapethissite.com -o test.txt`
- `python scraper.py -d https://www.startbase.com -o startbase.txt`

#Parser
- `python3 parser.py -f startbase.txt > val.csv`