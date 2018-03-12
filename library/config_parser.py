#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2018, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}

DOCUMENTATION = """
---
module: config_parser
author: Ansible Network Team
short_description: Parses the device configuration into Ansible facts
description:
  - This module will build on the C(text_parser) module in C(network-engine)
    parsing a device configuration file into Ansible facts.  It will load
    all parsers from the C(path) argument and generate a facts based on the
    rules in the parsing files.
version_added: "2.5"
options:
  src:
    description:
      - The source directory that contains the parser files.  This path
        should be a valid directory that contains all of the parser files
        to parse the device configuration.
    required: yes
    default: null
  config:
    description:
      - This argument should contain the device configuration text as
        retrieved from the node.  The data from this argument is used
        by the parsers to generate Ansible facts.
    required: yes
    default: null
"""

EXAMPLES = """
- name: load all parsers for network_os
  config_parser:
    src: "parsers/{{ ansible_network_os }}"
    config: "{{ lookup('file', 'files/device.cfg') }}"
"""

RETURN = """
ansible_network_config:
  description: top level key that contains the parsed configuration
  retured: always
included:
  description: the paths to the parser files that were used
  retured: always
"""
