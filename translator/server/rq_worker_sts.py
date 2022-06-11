import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from redis import Redis
from rq import Connection, SimpleWorker

from utils.utils import load_json_file

ROOT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    config = load_json_file(os.path.join(ROOT_DIR,"config", "config.json"))

    env_redis_host = os.environ.get('REDIS_HOST')
    if env_redis_host is not None:
        config['REDIS']['HOST'] = os.environ.get('REDIS_HOST')

    redis_config = config["REDIS"]

    redis_conn = Redis(host=redis_config["HOST"], port=redis_config["PORT"])
    with Connection(redis_conn):
        worker = SimpleWorker(["aa_queue"])
        worker.work()

if __name__ == '__main__':
    main()