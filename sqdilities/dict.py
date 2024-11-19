def combine(*args):
    if any([not isinstance(_, dict) for _ in args]):
        raise TypeError('All arguments must be dictionaries')

    return {**{key: value for d in args for key, value in d.items()}}
