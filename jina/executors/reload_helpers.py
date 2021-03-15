import os
import pickle
from typing import Union
import numpy as np


class DumpPersistor:
    @staticmethod
    def export_dump(path, data):
        # split into vectors and kv
        pickle.dump(data['ids'], open(os.path.join(path, 'ids.pkl'), 'wb'))
        pickle.dump(data['vectors'], open(os.path.join(path, 'vectors.pkl'), 'wb'))
        pickle.dump(data['kv'], open(os.path.join(path, 'kv.pkl'), 'wb'))

    @staticmethod
    def import_dump(path, content: Union['all', 'vector', 'kv']):
        # split into vectors and kv
        # TODO maybe split into separate functions based on 'content'
        if content == 'vector':
            return [['id1', 'id2', 'id3'], np.ones([3, 7])]
        elif content == 'kv':
            return [
                ['id1', 'id2', 'id3'],
                [
                    {
                        'id': 'id1',
                        'text': 'our text 1',
                        'embedding': np.ones(
                            [
                                7,
                            ]
                        ),
                    },
                    {
                        'id': 'id2',
                        'text': 'our text 2',
                        'embedding': np.zeros(
                            [
                                7,
                            ]
                        ),
                    },
                    {
                        'id': 'id3',
                        'text': 'our text 3',
                        'embedding': np.zeros(
                            [
                                7,
                            ]
                        ),
                    },
                ],
            ]
