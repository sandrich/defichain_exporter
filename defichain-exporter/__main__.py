import time
import random
import argparse
from jsonrpc_requests import Server
from prometheus_client import start_http_server, Gauge, Enum

def process_type(g, data):
    if g['type'] == 'gauge':
        g['obj'].set(data)
    else:
        g['obj'].state(str(data))

def process_masternodes(server, f):
    minting = server.getmintinginfo()
    for k, v in f.items():
        process_type(v, minting[k])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DefiChain Exporter')
    parser.add_argument('--username', help='rpc username')
    parser.add_argument('--password', help='rpc password')
    parser.add_argument('--port', help='exporter port (default 8000)', default=8000)
    parser.add_argument('--masternode', help='masternode host (default http://localhost:8554)', default='http://localhost:8554')

    args = parser.parse_args()

    start_http_server(args.port)

    server = Server(masternode, auth=(args.username, args.password))

    masternode_minting_functions = {
        "currentblockweight": { "type": "gauge", "obj" : Gauge('masternode__minting_current_blockweight', 'Current Blockweight')},
        "currentblocktx": { "type": "gauge", "obj" : Gauge('masternode_minting_current_blocktx', 'Current Blocktx')},
        "difficulty": { "type": "gauge", "obj" : Gauge('masternode_minting_difficulty', 'Difficulty')},
        'isoperator': { "type": "enum", "obj" : Enum('masternode_minting_isoperator', 'Is Operator', states = ["True", "False"])},
        'masternodestate': { "type": "enum", "obj" : Enum('masternode_minting_masternodestate', 'Masternode state', states = ["ENABLED", "PRE_ENABLED", "PRE_RESIGNED", "RESIGNED", "PRE_BANNED", "BANNED"])},
        "mintedblocks": { "type": "gauge", "obj" : Gauge('masternode_minting_mintedblocks', 'Minted blocks')}
    }


    while True:
        process_masternodes(server, masternode_minting_functions)
        time.sleep(random.random())