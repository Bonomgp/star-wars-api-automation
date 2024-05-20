#!/usr/bin/env bash

echo "Starting API automation run..."

# Start execution of tests:
robot --name 'API Test run' -d results/ tests.robot

echo "Automation run completed. Reports are available in the results directory."

exit 0
