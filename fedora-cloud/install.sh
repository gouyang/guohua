#!/bin/bash

name=fedora-cloud
iso=$name-cidata.iso

echo "
name=$name
iso=$iso
"

# - example using unix bridge br0
virt-install --name $name --ram 2048 --vcpu 2 --os-variant fedora21 --import --disk path=/var/lib/libvirt/images/Fedora-Cloud-Base-20141203-21.x86_64.raw,bus=virtio --disk path=/var/lib/libvirt/boot/$iso,device=cdrom --network bridge=br1,model=virtio --graphics vnc

exit
