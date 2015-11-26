Hi All 
This "configure" function use as new tugboat function.so using that you can get current version relate all server ip list to hosts file.Using that you can run any ansible playbook

if any issue contact me 
Kasun Rathnayaka 
gmail:kasunmaduraeng@gmail.com
linkedin:https://lk.linkedin.com/in/kasunmadurarathnayaka

Guide Line 
1. Get clone 
2. Add above config to __init_.py

__all__ = ["app", "infrastructure", "full_deploy", "show_config", "full_undeploy", "configure"]

# Import External Hooks from Hooks Directory

import_hooks(os.path.dirname(__file__))

@fabric.api.task
def configure(*args, **kwargs):
    sys.modules.get('hooks.app_custom').configure(*args, **kwargs)


3. then  copy  app_custom.py to hooks/

4. then run

fab configure:environment=$ENV,version=$Verssion


eg:
fab configure:environment=dev,version=1.1.6 


--- tugboat only for pearson :)---
