import numpy as np


def read_labels(fp: str, sep=',') -> list:
    """
    Read list of labels from given filepath
    :param fp: file path to read labels from
    :param sep: separator
    :return: list of labels
    """
    with open(fp) as fid:
        return list(map(lambda x: x.strip().lower(), fid.readline().split(sep)))


def get_choices(fp:str) -> tuple:
    """
    Create tuple of possible choices for the django.forms.ChoiceField
    :param fp: file path to list of possible choices:
    :return: tuple of items (value, value)
    """
    labels = read_labels(fp)
    return tuple([(item.lower(), item) for item in labels])


def get_feature_vector(selected_label: str, labels_fp: str, ordinal=False) -> np.array:
    """
    Build either One-Hot or Label encoded feature vector
    :param selected_label: what label is to be encoded
    :param labels_fp: file path to all labels
    :param ordinal: whether use Label encoding
    :return: encoded vector
    """
    labels = read_labels(labels_fp)
    idx = labels.index(selected_label)

    if ordinal:
        return np.asarray(idx + 1, dtype=np.float32)

    vec = np.zeros(len(labels), dtype=np.float32)
    vec[idx] = 1.0
    return vec


def calc_bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index
    """
    return weight / (height**2)


def normalize_to_range(value: float, min_allowed: float, max_allowed: float,
                       min: float, max: float) -> float:
    """
    Scale value from [min, max] to [min_allowed, max_allowed] range
    """
    return (max_allowed - min_allowed) * (value - min) / (max - min) + min_allowed
