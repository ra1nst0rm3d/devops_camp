#!/bin/bash
ansible-playbook setup.yaml -i inventory --ask-become-pass --vault-password-file pwd
