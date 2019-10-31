# stocks-portfolio
Stock portfolio and watch list management dashboard

Having recently started investing in stocks via Robinhood, I've often found myself craving features that are not supported by their mobile app. This (apart from the free Hacktoberfest t-shirt) motivated me to take up this project. But the more I think about it, I find myself coming up with extremly interesting ideas to enhance the project and build up my skill set.

**What follows is a long and growing list of feature ideas:**

- [ ] One page app with a basic user interface that lets me view and add stocks to my portfolio (with quantity) or watchlist
- [ ] Detailed view of a selected stock's historical performance
- [ ] Configurable time range to view statistics for
- [ ] Daily performance of portfolio + watchlist
- [ ] Portfolio + watchlist performance for a specific time range (missing feature)
- [ ] Intermediate alerting mechanism for price changes (missing feature)

**In addition to these features, I envision that I might be able to use this project as an avenue to learn about the following:**

- [ ] System design (initial design, and incorporating design changes)
    - [ ] Database model design
    - [ ] API design
    - [ ] UX
    - [ ] Backend algorithms and data structures
- [ ] Configuring and deploying a project on a cloud platform
- [ ] Comfort with full stack development
- [ ] Interactive visualizations using Python + libraries like d3.js
- [ ] Working with external APIs (e.g. [Alpha Vantage](https://www.alphavantage.co/documentation/)) with rate limitations
    - [ ] Making requests and parsing outputs
    - [ ] Smart fetch/prefetch to optimize unused rate limits (most excited about this!)

**Run Instructions:**

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install django
$ cd stocks_mgmt/
$ python manage.py migrate
$ python manage.py runserver
```

The server will be running at http://127.0.0.1:8000/dashboard/

If you would like to hack around on this project, or have any questions, feel free to reach out to me via email.
