import threading
from typing import Optional

from jina.drivers import BaseExecutableDriver

# DEBUG_MODE = True
DEBUG_MODE = False


class ReloadControlReqDriver(BaseExecutableDriver):
    def __init__(
        self,
        executor: Optional[str] = None,
        *args,
        **kwargs,
    ):
        super().__init__(executor, 'reload', *args, **kwargs)

    def __call__(self, *args, **kwargs):
        fn = getattr(self.exec, 'reload_compound')
        if DEBUG_MODE:  # just to have breakpoints working
            fn(self.req.path)
        else:
            self.thread = threading.Thread(target=fn, args=(self.req.path,))
            self.thread.start()
