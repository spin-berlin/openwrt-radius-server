IMAGE_BUILDER=OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64
PROFILES=TLWDR4300 MYNETN600
PACKAGES="-wpad-mini wpad \
	ip tmux \
	freeradius2 \
	freeradius2-common \
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
  freeradius2-mod-radutmp \
	kmod-batman-adv"

images: ${IMAGE_BUILDER} ${PROFILES}
	@echo "Images created for all profiles."

${PROFILES}: %:
	$(MAKE) -C $(IMAGE_BUILDER) image PROFILE=$* \
		PACKAGES=$(PACKAGES) \
		FILES="$(CURDIR)/files" \
		BIN_DIR="$(CURDIR)/images" ; \

OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64: OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64.tar.bz2
	tar -xvf dl/OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64.tar.bz2

OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64.tar.bz2:
	cd dl && wget -c http://downloads.openwrt.org/snapshots/trunk/ar71xx/OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64.tar.bz2

random:
	dd if=/dev/urandom of=$(CURDIR)/files/etc/freeradius2/certs/random count=2
dh:
	openssl dhparam -out $(CURDIR)/files/etc/freeradius2/certs/dh 1024

clean:
	rm images/*
