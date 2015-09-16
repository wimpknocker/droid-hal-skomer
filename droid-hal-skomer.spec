# These and other macros are documented in dhd/droid-hal-device.inc
%define device skomer
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty XCover 2

%define installable_zip 1

%define have_custom_img_boot 1
%define have_custom_img_recovery 1

%define straggler_files \
/boot/hybris-updater-script \
/boot/hybris-updater-unpack.sh \
/boot/update-binary \
/selinux_version \
/service_contexts
%{nil}

%include rpm/dhd/droid-hal-device.inc
