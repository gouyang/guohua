#!/bin/bash

name=fedora-cloud
iso=$name-cidata.iso

# create meta-data file
echo -e "instance-id: fedora-cloud0\nlocal-hostname: fedora-cloud-00" > meta-data

# - create user-data file
echo -e "#cloud-config\npassword: fedora\nchpasswd: {expire: False}\nssh_pwauth: True" > user-data

# - clean out old stale iso files
rm -f $iso /var/lib/libvirt/boot/$iso
# - create latest iso with cloud-init files
genisoimage -output $iso -volid cidata -joliet -rock user-data meta-data
# - copy cloud-init iso into place
scp $iso /var/lib/libvirt/boot/$iso


# - copy down RHEL Atomic image
#wget http://download.fedoraproject.org/pub/fedora/linux/releases/21/Cloud/Images/x86_64/Fedora-Cloud-Base-20141203-21.x86_64.raw.xz

# - decompress image
echo "- decompressing image may take a while"
xz -d /var/lib/libvirt/images/Fedora-Cloud-Base-20141203-21.x86_64.raw.xz
cp Fedora-Cloud-Base-20141203-21.x86_64.raw /var/lib/libvirt/images/

exit
