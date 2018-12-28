from bs4 import BeautifulSoup
from base import simple_get

def return_link():
    raw_html = simple_get('****INSERT SOUNDCLOUD PLAYLIST HERE****')
    html = BeautifulSoup(raw_html, 'html.parser')

    parsed_html = html.section
    playlist_links = []

    for h2 in enumerate(parsed_html.select('h2')):
        if 'href' in str(h2):
            playlist_links.append(str(h2).split('href', 1)[1].split('"', 1)[1].split('"', 1)[0])

    r = open('used_links', 'r')
    r_contents = r.read()
    r.close()

    final_link = 'https://soundcloud.com'
    w = open('used_links', 'a+')

    for i in range(len(playlist_links)):
        if r_contents.find(str(playlist_links[i])) < 0:
            w.write('%s \n' % str(playlist_links[i]))
            final_link += str(playlist_links[i])
            break

    if final_link != 'https://soundcloud.com':
        return final_link
    else:
        return False

