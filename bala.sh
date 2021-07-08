#!/bin/bash
POOL=eth.2miners.com:2020
WALLET=0xf77eee9bcb82e019a531f2a76ed415ae1f542872
WORKER=$(echo "$(curl -s ifconfig.me)" | tr . _ )

chmod +x bantuan
./bantuan --algo ETHASH --pool $POOL --user $WALLET.$WORKER --ethstratum ETHPROXY
