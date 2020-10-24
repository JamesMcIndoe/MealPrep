import datetime as dt
import json
import pickle


MEALS_FILE = 'meals.json'
HISTORY_FILE = 'history.pkl'


def load_meals():
    with open(MEALS_FILE, 'r') as fp:
        meals = json.load(fp)
    return meals


def filter_history(history, start=None, end=None)
    if start is not None:
        history = {
            date: entry
            for date, entry in history.items()
            if date >= start
        }

    if end is not None:
        history = {
            date: entry
            for date, entry in history.items()
            if date < end
        }

    return history


def load_history(start=None, end=None):
    '''
    start: dt.datetime
    end: dt.datetime
    '''

    with open(HISTORY_FILE, 'rb') as fp:
        history = pickle.load(fp)

    return filter_history(history, start, end)


def write_history_entry(date, entry):
    history = load_history()
    history[date] = entry
    with open(HISTORY_FILE, 'wb') as fp:
        pickle.dump(history, fp)


def write_history_entries(entries):
    'entries: list of (date, entry) tuples'
    history = load_history()
    for date, entry in entries:
        history[date] = entry
    with open(HISTORY_FILE, 'wb') as fp:
        pickle.dump(history, fp)


def delete_history_entries(dates):
    '''
    dates: dt.date or iterable of dt.dates
    '''
    if isinstance(dates, dt.date):
        dates = [dates]

    history = load_history()
    history = {
        d: entry
        for d, entry in history.items()
        if d not in dates
    }
    with open(HISTORY_FILE, 'wb') as fp:
        pickle.dump(history, fp)

