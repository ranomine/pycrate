# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_gmr1_csn1/packet_paging_request_message_content.py
# * Created : 2023-10-24
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: ETSI TS 101 376-04-12
# section: 11.2.10 Packet Paging Request (A/Gb mode only)
# top-level object: Packet Paging Request message content

# external references
from pycrate_gmr1_csn1.padding_bits import padding_bits

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

repeated_page_info_struct = CSN1Alt(name='repeated_page_info_struct', alt={
  '0': ('', [
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='reserved', bit=32)]),
    '1': ('', [
    CSN1Bit(name='length_of_reserved_field', bit=4),
    CSN1Bit(name='reserved', bit=8, num=([1], lambda x: x))])})]),
  '1': ('', [
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='tmsi', bit=32)]),
    '1': ('', [
    CSN1Bit(name='length_of_mobile_identity_contents', bit=4),
    CSN1Bit(name='mobile_identity', bit=8, num=([1], lambda x: x))])}),
  CSN1Bit(name='channel_needed', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reserved', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='msc_id', bit=6)])})])})

packet_paging_request_message_content = CSN1List(name='packet_paging_request_message_content', trunc=True, list=[
  CSN1Bit(name='reserved', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reserved', bit=16)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reserved', bit=2)])}),
  CSN1List(list=[
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='repeated_page_info', obj=repeated_page_info_struct)]),
    CSN1Val(name='', val='0'),
    CSN1Ref(obj=padding_bits)])])

