#!/bin/bash
# Simple iptables IP/subnet block script 
# -------------------------------------------------------------------------
# Copyright (c) 2021 pctripsesp project 
# This script is licensed under GNU GPL version 2.0 or above
# ----------------------------------------------------------------------
IPT=/sbin/iptables
SPAMLIST="spamlist"
SPAMDROPMSG="SPAM LIST DROP"
BADIPS=$(egrep -v -E "^#|^$" /root/iptables/black.list)
 
# create a new iptables list
$IPT -N $SPAMLIST 2>/dev/null
 
for ipblock in $BADIPS
do	
#CHECK IF ALREADY EXISTS
$IPT -C $SPAMLIST -s $ipblock -j DROP 2>/dev/null
CHECK=$?
if [[ "$CHECK" -eq "1" ]]; then
       $IPT -A $SPAMLIST -s $ipblock -j LOG --log-prefix "$SPAMDROPMSG"
       $IPT -A $SPAMLIST -s $ipblock -j DROP
fi 
done

## CHECK IF LIST ALREADY APPLIED
$IPT -C INPUT -j $SPAMLIST 2>/dev/null
CHECK_LIST=$?
if [[ "$CHECK" -eq "2" ]]; then
	$IPT -I INPUT -j $SPAMLIST
	$IPT -I OUTPUT -j $SPAMLIST
	$IPT -I FORWARD -j $SPAMLIST
fi
