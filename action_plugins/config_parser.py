# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
import os

from ansible import constants as C
from ansible.plugins.action import ActionBase
from ansible.module_utils._text import to_text

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

def warning(msg):
    if C.ACTION_WARNINGS:
        display.warning(msg)


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):

        result = super(ActionModule, self).run(tmp, task_vars)

        try:
            src = self._task.args['src']
            contents = self._task.args['config']
        except KeyError as exc:
            return {'failed': True, 'msg': 'missing required argument: %s' % to_text(exc)}

        if not os.path.exists(src) or not os.path.isdir(src):
            warning('`src` path is not valid directory or does not exist')
            result['ansible_facts'] = {'ansible_network_config': {}}
            return result

        new_task = self._task.copy()

        new_task.args = {
            'dir': src,
            'contents': contents
        }

        kwargs = {
            'task': new_task,
            'connection': self._connection,
            'play_context': self._play_context,
            'loader': self._loader,
            'templar': self._templar,
            'shared_loader_obj': self._shared_loader_obj
        }

        task_parser = self._shared_loader_obj.action_loader.get('text_parser', **kwargs)
        resp = task_parser.run(task_vars=task_vars)

        if resp.get('failed') is True:
            return resp

        network_config = resp.get('ansible_facts') or {}
        result['ansible_facts'] = {'ansible_network_config': network_config}
        result['included'] = resp['included']

        return result

