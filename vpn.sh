#!/bin/sh

# vpn.sh
# by ginglis
# for connecting to the eduroam vpn
# requires openconnect application
# requires two factor authentication

# kill if it's running already
killall openconnect

# requires sudo privileges to run
sudo openconnect --protocol=anyconnect --no-dtls --passwd-on-stdin vpnaccess.nd.edu/mfa -s /etc/vpnc/vpnc-script

# or you can alias is to vpn, which is what I do
# alias vpn='sudo openconnect --protocol=anyconnect --no-dtls --passwd-on-stdin vpnaccess.nd.edu/mfa -s /etc/vpnc/vpnc-script'

# if you don't want to sign in every time, you can do this:
# alias vpn='echo "YOUR_PASSWORD" | sudo openconnect --protocol=anyconnect --no-dtls --user=YOUR_USERNAME --passwd-on-stdin vpnaccess.nd.edu/mfa -s /etc/vpnc/vpnc-script'
