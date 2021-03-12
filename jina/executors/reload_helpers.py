from typing import Union


class DumpPersistor:
    @staticmethod
    def export_dump(path, data):
        # split into vectors and kv
        raise NotImplementedError

    @staticmethod
    def import_dump(path, content: Union['all', 'vectors', 'kv']):
        # split into vectors and kv
        # TODO maybe split into separate functions based on 'content'
        raise NotImplementedError
