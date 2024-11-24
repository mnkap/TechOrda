#!/bin/bash

cd /tmp # temporary location for convenience
curl -LO https://github.com/jusan-singularity/track-devops-systemd-api/releases/download/v0.1/api # downloading api file
chmod 755 api # make api executable
# какие-то команды для настройки
sudo cp /tmp/systemd-service-api/api.service /usr/lib/systemd/system/

sudo systemctl start api
