#!/usr/bin/env python3

import random
import requests
import threading


def get_topstories():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    topstories = requests.get(url)
    if topstories.ok:
        return topstories.json()
    raise ConnectionError('''Problem getting top stories.''')


def get_story(story_id):
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json'.format(story_id)
    story = requests.get(url)
    if story.ok:
        return story.json()
    raise ConnectionError('''Problem getting story details.''')


def print_story(story_id):
    s = get_story(story_id)
    print('{} ({})'.format(s['title'], s['score']))


def print_top(num=None):
    if num is None:
        stories = get_topstories()
    else:
        stories = get_topstories()[:num]
    threads = [threading.Thread(target=print_story, args=(s,))
               for s in stories]

    for t in threads:
        t.start()


def print_random():
    stories = get_topstories()
    story = random.choice(stories)
    print_story(story)


def print_url_if_pdf(story_id):
    s = get_story(story_id)
    if s['title'].lower().find('pdf') != -1:
        print('{} ({}) - {}'.format(s['title'], s['score'], s['url']))


def print_pdfs_with_urls():
    stories = get_topstories()
    threads = [threading.Thread(target=print_url_if_pdf, args=(s,))
               for s in stories]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    print('--- Random story ---')
    print_random()
    print('--- Top 8 stories ---')
    print_pdfs_with_urls()
