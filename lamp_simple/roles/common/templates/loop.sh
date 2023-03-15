#!/bin/sh

INDEX=1
LINE_NUM=1

while read LINE
do
        echo "${LINE_NUM}: ${LINE}"
        ((LINE_NUM++))

done < /etc/fstab

echo -e  "*************************************************************************************\n\n\n\n\n\\n\n"
grep nfs /etc/fstab | while read LINE
do
        echo "nfs: ${LINE}"

done



while true
do
        read -p "1: show disk usage. 2: show uptime. " CHOICE
        case "$CHOICE"  in
        1)
        df -h
        ;;
        2)
        uptime
        ;;
        *)
        break
        ;;

esac
done

while [ $INDEX -lt 5 ]
do
        echo "Creating directory-${INDEX}"
        mkdir /home/jorge/directory-${INDEX}
        ((INDEX++))
done
        rmdir /home/jorge/directory-*


FS_NUM=1

grep xfs /etc/fstab | while read FS MP REST
do
        echo "${FS_NUM}: file system: ${FS}
        echo "${FS_NUM}: mount point: ${MP}
        ((FS_NUM++))

done

