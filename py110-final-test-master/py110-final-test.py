import json
import re
from typing import Dict, Iterable


def user_generator(file_path: str) -> Iterable[Dict]:
    with open(file_path, 'r') as f:
        data = json.loads(f.read())
        for i in data:
            yield i


def dropper(func):
    def wrapper(file, drop_incorrect):
        f = func(file)
        for user in f:
            if drop_incorrect:
                if type(user['name'] is str) and re.fullmatch(r'^([A-Z][a-z]+)$', str(user['name'])):
                    if type(user['surname'] is str) and re.fullmatch(r'^([A-Z][a-z]+)$', str(user['surname'])):
                        if type(user['sex'] is str) and re.fullmatch(r'([mf])', str(user['sex'])):
                            if type(user['age']) is int and 17 < user['age'] < 100:
                                if type(
                                        user['contacts']['email']) is str or None and re.fullmatch(
                                    r'^[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}$',
                                    str(user['contacts'][
                                            'email'])):
                                    if type(
                                            user['contacts']['tel']) is str or None and re.fullmatch(
                                        r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', str(user['contacts']['tel'])):
                                        if type(
                                                user['contacts']['site']) is str or None and re.fullmatch(
                                            r'([-a-zA-Z0-9@:%_+.~#?&/=]{2,256}\.[a-z]{2,4}\b(/['
                                            r'-a-zA-Z0-9@:%_+.~#?&/=]*)?)',
                                            str(user['contacts']['site'])):
                                            yield user
            else:
                yield user

        return user
    return wrapper
