# DefiChain Exporter
Prometheus exporter for DefiChain Masternodes [defichain.io](defichain.io)

## Installation

```
pip3 install defichain-exporter
```

## Usage
By default defichain-exporter will run on port 8000 and run in foreground. Ideally this is installed into a daemon service such as systemd.

```
usage: defichain-exporter [-h] [--username USERNAME] [--password PASSWORD]
                          [--port PORT] [--masternode MASTERNODE]

DefiChain Exporter

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME   rpc username
  --password PASSWORD   rpc password
  --port PORT           exporter port (default 8000)
  --masternode MASTERNODE
                        masternode host (default http://localhost:8554)
```

## License
MIT

