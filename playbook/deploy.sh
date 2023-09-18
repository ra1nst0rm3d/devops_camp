#!/bin/bash
ansible-playbook setup.yaml -i inventory --vault-password-file pwd
