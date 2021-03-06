#
# Author:: Noah Kantrowitz <noah@coderanger.net>
#
# Copyright 2014, Balanced, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from fabric.api import task, local
from fabric.decorators import roles

@roles('www')
@task
def one():
    """Task one."""
    local('echo one')


@task
def two(arg1):
    """Task
    two."""
    local('echo two %s'%(arg1,))

@task
@roles('www')
def three(c, d=1):
    """Take three."""
    local('echo three %s %s'%(c, d))
