import os
import fabric
import urllib2
import json
import time

from fabric.api import local, sudo, run
from tugboat.deployment import operations, events
from tugboat.decorators import deployment

from tugboat.utils import tugboat_context as __tugboat_context
from tugboat.deployment.app.operations import app_servers as __app_servers
from tugboat.deployment.app.tasks import activate, record_deployment

def simple(*args,**kwargs):
	run('uname -a')
