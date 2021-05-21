import time
import random
import argparse
from jsonrpc_requests import Server, TransportError
from prometheus_client import start_http_server, Gauge, Enum

def call_rpcfunc(f):
    '''
    Takes an rpcfunction as parameter and safely calls it. Returns object if correctly executed, otherwise fails with an error.
    '''
    try:
        retval = f()
        return(retval)
    except TransportError as transport_error:
        if '401' in str(transport_error):
            print("Authentication failed. Please check username and password!")
            exit()
        else:
            print(transport_error)
            exit()

def process_type(g, data):
    if g['type'] == 'gauge':
        g['obj'].set(data)
    else:
        g['obj'].state(str(data))

def process_masternode_minting(server, f):
    '''
    Current master node specific metrics
    '''
    minting = call_rpcfunc(server.getmintinginfo)
    for k, v in f.items():
        process_type(v, minting[k])

def main():
    parser = argparse.ArgumentParser(description='DefiChain Exporter')
    parser.add_argument('--username', help='rpc username')
    parser.add_argument('--password', help='rpc password')
    parser.add_argument('--port', help='exporter port (default 8000)', default=8000)
    parser.add_argument('--masternode', help='masternode host (default http://localhost:8554)', default='http://localhost:8554')

    args = parser.parse_args()

    start_http_server(args.port)

    server = Server(args.masternode, auth=(args.username, args.password))

    masternode_minting_functions = {
        "currentblockweight": { "type": "gauge", "obj" : Gauge('masternode__minting_current_blockweight', 'Current Blockweight')},
        "currentblocktx": { "type": "gauge", "obj" : Gauge('masternode_minting_current_blocktx', 'Current Blocktx')},
        "difficulty": { "type": "gauge", "obj" : Gauge('masternode_minting_difficulty', 'Difficulty')},
        'isoperator': { "type": "enum", "obj" : Enum('masternode_minting_isoperator', 'Is Operator', states = ["True", "False"])},
        'masternodestate': { "type": "enum", "obj" : Enum('masternode_minting_masternodestate', 'Masternode state', states = ["ENABLED", "PRE_ENABLED", "PRE_RESIGNED", "RESIGNED", "PRE_BANNED", "BANNED"])},
        "mintedblocks": { "type": "gauge", "obj" : Gauge('masternode_minting_mintedblocks', 'Minted blocks')}
    }

    while True:
        process_masternode_minting(server, masternode_minting_functions)
        time.sleep(random.random())

if __name__ == '__main__':
    main()