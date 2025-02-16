#!/bin/sh
python="./python"
# run ./venv.sh before running the program
if [ "$(basename $(pwd))" = "Trial_Project" ]; then
    $python -m venv venv
    source venv/bin/activate
    which python
    python -m pip install -U pip
    python -m pip install beautifulsoup4 lxml requests
else
    echo "You are not in the Trial_Project directory"
fi
