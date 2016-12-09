import plugin
import time


def bk(irc, user, target, msg):
    menu = ['Whopper Cheese',
            'Western Whooper',
            'Cheeseburger XXL',
            'Chicken Whopper',
            'Whopper',
            'Fish King',
            'Deluxe Chicken']

    day = int(time.strftime('%w'))
    today = time.strftime("%Y.%m.%d")
    line = 'Menu for %s @ Burger King: %s' % (today, menu[day])
    irc.msg(target, line)

plugin.add_plugin('^!bk\Z', bk)
plugin.add_help('!bk', 'Query Burger King menu')