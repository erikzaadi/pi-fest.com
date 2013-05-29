#!/bin/bash
git submodule update --init
if [[ ! -d "${PWD}/.venv" ]]; then
    echo "Creating virtual env.."
    virtualenv .venv > /dev/null
    virtualenv --relocatable .venv > /dev/null
else
    echo "Using existing virtualenv.."
fi
source ./.venv/bin/activate
pip install -r ./requirements.txt
make html
