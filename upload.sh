#!/bin/bash

git push

ssh root@192.168.1.117 'cd /opt/json_server/Jserver/; git pull'
