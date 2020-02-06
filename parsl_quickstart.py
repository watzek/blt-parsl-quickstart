import parsl
from parsl.app.app import python_app, bash_app
from parsl.config import Config
from parsl.providers import GridEngineProvider
from parsl.executors import HighThroughputExecutor
from parsl.executors import ThreadPoolExecutor
from parsl.addresses import address_by_route, address_by_query, address_by_hostname

config = Config(
    executors=[HighThroughputExecutor(worker_debug=True, cores_per_worker=16,
                                      address=address_by_route(),
                                      provider=GridEngineProvider(walltime='10000:00:00', nodes_per_block=1,
                                                                  init_blocks=1,
                                                                  max_blocks=4, scheduler_options="#$ -pe smp 48"),
                                      label="workers")
               ],
)


parsl.set_stream_logger()
parsl.load(config)
