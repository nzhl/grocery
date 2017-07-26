from os.path import join, expanduser

LOGIN_URL = "http://moodle.nottingham.ac.uk/login/index.php"
INDEX_URL = "http://moodle.nottingham.ac.uk/my/"
SEARCH_URL = "http://www.xiami.com/search/?key="
XML_URL = "http://www.xiami.com/song/playlist/id/"


DATA_PATH = join(expanduser('~'), '.nmterminal')
SONG_PATH = join(DATA_PATH, 'song')
LOG_PATH = join(DATA_PATH, 'log')
COOKIE_PATH = join(DATA_PATH, 'cookies')


HEADERS = {
'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'),
}
