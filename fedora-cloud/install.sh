#!/bin/bash

dir=$(basename $(pwd))
name=${dir-fedora-cloud}
iso=$name-cidata.iso
image=${image-yourimg}

echo "
name=$name
iso=$iso
"

# - example using unix bridge br1
virt-install --name $name --ram 2048 --vcpu 2 --os-variant fedora22 --import --disk path=$image,bus=virtio --disk path=/var/lib/libvirt/boot/$iso,device=cdrom --network bridge=br1,model=virtio --graphics vnc

exit
