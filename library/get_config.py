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
"""

EXAMPLES = """
- name: return the current device config
  get_config:
"""

RETURN = """
text:
  description: The device running configuration as text
  returned: always
  type: str
  sample: "hostname localhost\nip domain-name ansible.com"
"""
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection


def main():
    """main entry point for module execution
    """
    argument_spec = dict(
        source=dict(default='running', choices=['running', 'startup'])
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    source = module.params['source']

    connection = Connection(module._socket_path)
    output = connection.get_config(source=source)

    result = {
        'changed': False,
        'text': output
    }

    module.exit_json(**result)


if __name__ == '__main__':
    main()
