pager-reports
================

Pull notes from pagerduty and adds it to reports

Requirements
------------

* Python 2.7
* Pip
* Python venv (optional)

Installation
------------

#### Install virtual env (Optional)
`sudo -EH pip install virtualenv`

#### Clone the repo
`git clone https://github.com/nclouds/pager-reports.git`

### Replace the API_KEY

Replace <YOUR_API_KEY> with your own pagerduty key in get_reports.py (read-only api key will work)

#### Active virtual env and install the requirements
`cd pager-reports`

`source bin/active` (Opional if you are not using virtualenv)

`pip install -r requirements.txt` (Might need sudo, if not using virtual env)

#### Run the script
`./get_reports.py`

#### Get help
`./get_reports.py --help`
