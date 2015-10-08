#!/bin/bash

name=fedora-cloud
iso=$name-cidata.iso

echo "
name=$name
iso=$iso
"

virsh destroy $name
virsh undefine $name
virsh vol-delete --pool default /var/lib/libvirt/images/$name*
virsh pool-refresh default

rm -f $iso meta-data user-data
rm -f /var/lib/libvirt/images/$name*

exit

