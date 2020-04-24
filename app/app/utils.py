def get_choices(fp):
    with open(fp) as fid:
        choices = map(lambda x: x.strip(), fid.readline().split(','))
        return tuple([(item.lower(), item) for item in choices])
