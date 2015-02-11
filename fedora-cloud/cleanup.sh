#!/bin/bash

name=fedora-cloud
iso=$name-cidata.iso

echo "
name=$name
iso=$iso
"

virsh destroy $name
virsh undefine $name
virsh vol-delete --pool default /var/lib/libvirt/images/Fedora-Cloud-Base-20141203-21.x86_64.raw
virsh pool-refresh default

rm -f $iso meta-data user-data

exit

