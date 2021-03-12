import os
import pickle
from typing import Union


class DumpPersistor:
    @staticmethod
    def export_dump(path, data):
        # split into vectors and kv
        pickle.dump(data['ids'], open(os.path.join(path, 'ids.pkl'), 'wb'))
        pickle.dump(data['vectors'], open(os.path.join(path, 'vectors.pkl'), 'wb'))
        pickle.dump(data['kv'], open(os.path.join(path, 'kv.pkl'), 'wb'))

    @staticmethod
    def import_dump(path, content: Union['all', 'vectors', 'kv']):
        # split into vectors and kv
        # TODO maybe split into separate functions based on 'content'
        if content == 'vectors':
            return [[1], [2], [3]]
        elif content == 'kv':
            return [
                {'a': 1},
                {'a': 2},
                {'a': 3}
            ]
