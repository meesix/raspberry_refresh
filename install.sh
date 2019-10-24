#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

echo "Installing system service"
cp ./setup/izone_refresh.service /etc/systemd/system
systemctl daemon-reload
echo "Starting service"
systemctl start izone_refresh
echo "All done."
