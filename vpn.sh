#!/bin/sh

# vpn.sh
# by ginglis
# for connecting to the eduroam vpn
# requires openconnect application
# requires two factor authentication

# kill if it's running already
killall openconnect

# requires sudo privileges to run
sudo openconnect vpnaccess.nd.edu/mfa 

# or you can alias is to vpn, which is what I do
# alias vpn='sudo openconnect vpnaccess.nd.edu/mfa'

# if you don't want to sign in every time, you can do this:
# alias vpn='echo "YOUR_PASSWORD" | sudo openconnect --user=YOUR_USERNAME --passwd-on-stdin vpnaccess.nd.edu/mfa'
