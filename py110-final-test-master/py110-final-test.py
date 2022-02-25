import json
import re
from typing import Dict, Iterable


def user_generator(file_path: str) -> Iterable[Dict]:
    with open(file_path, 'r') as f:
        data = json.loads(f.read())
        for i in data:
            yield i


def dropper(func):
    def wrapper(file, drop_incorrect=True):
        f = func(file)
        for user in f:
            if drop_incorrect:
                if isinstance(user['name'], str) and re.fullmatch(r'^([A-Z][a-z]+)$', str(user['name'])):
                    if isinstance(user['surname'], str) and re.fullmatch(r'^([A-Z][a-z]+)$', str(user['surname'])):
                        if isinstance(user['sex'], str) and re.fullmatch(r'([mf])', str(user['sex'])):
                            if isinstance(user['age'], int) and 17 < user['age'] < 100:
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


if __name__ == "__main__":
    count = 0
    for user in dropper(user_generator)("users_2240.json"):
        count += 1
    print(count)
