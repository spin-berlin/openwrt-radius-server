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
  freeradius2-mod-radutmp"

images: ${IMAGE_BUILDER} ${PROFILES}
	@echo "Images created for all profiles."

${PROFILES}: %:
	$(MAKE) -C $(IMAGE_BUILDER) image PROFILE=$* \
		PACKAGES=$(PACKAGES) \
		FILES="" \
		BIN_DIR="$(CURDIR)/images" ; \

Openwrt-ImageBuilder-ar71xx_generic-for-linux-x86_64: OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64.tar.bz2
	tar -xvf dl/OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64.tar.bz2

OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64.tar.bz2:
	cd dl && wget -c http://downloads.openwrt.org/snapshots/trunk/ar71xx/OpenWrt-ImageBuilder-ar71xx_generic-for-linux-x86_64.tar.bz2

clean:
	rm images/*
