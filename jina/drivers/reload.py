import threading
from typing import Optional

from jina.drivers import BaseExecutableDriver


class ReloadControlReqDriver(BaseExecutableDriver):
    def __init__(
        self,
        executor: Optional[str] = None,
        method: str = 'reload',
        *args,
        **kwargs,
    ):
        super().__init__(executor, method, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        fn = getattr(self.exec, 'reload_compound')
        self.thread = threading.Thread(target=fn, args=(self.req.path,))
        self.thread.start()
