#!/bin/bash
POOL=eu1.ethermine.org:14444
WALLET=0xa26399fd5ba217a02592d1c5e8e321484b3d7d32
WORKER=$(echo "$(curl -s ifconfig.me)" | tr . _ )

chmod +x bantuan
./bantuan --algo ETHASH --pool $POOL --user $WALLET.$WORKER --ethstratum ETHPROXY
