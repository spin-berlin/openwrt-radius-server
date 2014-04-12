# radius server for spin network

## Install on openwrt

First install some base packages:

    opkg update
    opkg install tmux ip

    opkg remove wpad-mini
    # wpad supports e.g. crypted adhoc
    opkg install wpad

Next install freeradius packages:

    opkg install freeradius2-common \
      freeradius2-mod-chap \
      freeradius2-mod-eap \
      freeradius2-mod-eap-gtc \
      freeradius2-mod-eap-md5 \
      freeradius2-mod-eap-mschapv2 \
      freeradius2-mod-eap-peap \
      freeradius2-mod-eap-tls \
      freeradius2-mod-eap-ttls \
      freeradius2-mod-exec \
      freeradius2-mod-files \
      freeradius2-mod-mschap \
      freeradius2-mod-pap \
      freeradius2-mod-radutmp

On a testing system you can also install the demo-certs:

    opkg install freeradius2-democerts

Don't do this on a production system!

## Generate certs and keys

Follow the instructions mentioned here:

https://github.com/FreeRADIUS/freeradius-server/blob/master/raddb/certs/README

Upload the ca.pem and server.pem to the router.

## Configure GTC

For now we use GTC authentication method so we can store passwords as salted
sha1. Uncomment the `gtc` section and `auth_type = PAP` in
`/etc/freeradius2/eap.conf`.
