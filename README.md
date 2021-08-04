* [Visit website](https://tasty-news.herokuapp.com/)


# Tasty News

Website created for personal purposes. It scrapes data from several other websites and shows the titles of the articles with link to main article.
In addition it store all articles in database and show some statistics in subpage.

Main View:
![Window view](https://github.com/mateuszwwwrobel/Tasty_News/blob/master/static/img/preview_1.png?raw=true)

Statistics View:
![Window view](https://github.com/mateuszwwwrobel/Tasty_News/blob/master/static/img/preview_2.png?raw=true)

## Getting Started

If you would like to visit a website please click a link below:
(first load may take a bit longer due to herokuapp sleeping.)

* [Visit website](https://tasty-news.herokuapp.com/)

## Technologies:

Project built with:
- Django,
- BeautifulSoup
- Bootstrap,
- Chart.js,

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/mateuszwwwrobel/Tasty_News.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv <venv-name>
$ source <venv-name>/bin/activate
```

Then install the dependencies:

```sh
(<venv-name>)$ pip install -r requirements.txt
```
Note the `(venv-name)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(<venv-name>)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`


## Authors

Wrobel Mateusz

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

For help with every trouble:
* [Stackoverflow](https://stackoverflow.com/)
