#!/bin/bash -e

# Any arguments you supply will be passed on to the test runner (nosetests).
# e.g. to run a single test:
#  ./run_tests.sh <pythonfilename>

cd `dirname ${BASH_SOURCE[0]}`
NOSE=${NOSE:-nosetests}
PYTHONPATH=../docker_manager $NOSE -v --where . --nocapture "$@"

