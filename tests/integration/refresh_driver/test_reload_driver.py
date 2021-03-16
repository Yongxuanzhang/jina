"""
create two indices (differnet)

first is loaded when we start
-- use for search reqs

-- control req (add # simulate time.sleep in the Compound)
-- 10sec query
-- at some point the sleep will end and we should see data from second index (and ONLY)
-- validate (once we see new only see new)
"""
import os
import time
from threading import Thread

from jina import Flow, Document
import numpy as np

from tests import get_documents


def test_reload(tmpdir):
    from jina.peapods.zmq import Zmqlet, send_ctrl_message

    # docs1 = [Document(text='abc', embedding=np.ones([12])) for _ in range(10)]
    # docs2 = [Document(text='xyz', embedding=np.zeros([12])) for _ in range(10)]

    # os.environ["JINA_WORKSPACE_CRUD"] = 'first_workspace'
    # with Flow.load_config('flow_index.yml') as flow_index1:
    #     flow_index1.index(docs1)
    #
    # os.environ["JINA_WORKSPACE_CRUD"] = 'second_workspace'
    # with Flow.load_config('flow_index.yml') as flow_index2:
    #     flow_index2.index(docs2)

    # def validate_results(resp):
    #     print('## resp', resp)

    def validate_results_empty(resp):
        print(f'### {resp}')
        for d in resp.docs:
            assert len(d.matches) == 0

    def validate_results_nonempty(resp):
        print(f'### {resp}')
        for d in resp.docs:
            assert len(d.matches) > 0

    def error_callback(resp):
        print(f'## error: {resp}')

    docs = list(
        get_documents(
            chunks=0, same_content=False, nr=1, index_start=0, same_tag_content=False
        )
    )

    def dump_reload(flow_query, flow_index, path):
        flow_index.dump(path)
        flow_query.reload(path)
        time.sleep(10)

    new_docs = list(
        get_documents(
            chunks=0, same_content=False, nr=1, index_start=1, same_tag_content=False
        )
    )

    DUMP_PATH = "some_path"
    os.environ["HW_WORKDIR"] = str(tmpdir)
    with Flow.load_config('flow_query.yml') as flow_query:
        with Flow.load_config('flow_index.yml') as flow_index:
            # TODO add DumpRequest and .dump method
            print(f'### first search')
            flow_query.search(docs, on_done=validate_results_empty)
            flow_index.index(new_docs)
            Thread(
                target=dump_reload,
                args=(
                    flow_query,
                    flow_index,
                    DUMP_PATH,
                ),
            ).start()
            print(f'### second search (empty)')
            flow_query.search(docs, on_done=validate_results_empty)
            for _ in range(100):
                flow_index.index(new_docs)
                flow_query.search(docs, on_done=validate_results_empty)
            # MAKE SURE THE THREAD IS DONE
            time.sleep(5)
            print(f'### third search (not empty)')
            flow_query.search(docs, on_done=validate_results_nonempty)

            # send_ctrl_message(ctrl_addr, 'RELOAD', timeout=100)
            # print(ctrl_addr)
