#!/usr/bin/env python3

import random
import requests


def get_topstories():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    topstories = requests.get(url)
    if topstories.ok:
        return topstories.json()
    raise Exception('''Problem getting top stories.''')


def get_story(story_id):
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json'.format(story_id)
    story = requests.get(url)
    if story.ok:
        return story.json()
    raise Exception('''Problem getting story details.''')


def print_top(num=8):
    stories = get_topstories()[:num]
    for story in stories:
        s = get_story(story)
        print('{} ({})'.format(s['title'], s['score']))


def print_random():
    stories = get_topstories()
    story = random.choice(stories)
    s = get_story(story)
    print('{} ({})'.format(s['title'], s['score']))


if __name__ == '__main__':
    print('--- Random story ---')
    print_random()
    print('--- Top 8 stories ---')
    print_top()
