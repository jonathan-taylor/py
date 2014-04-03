################Configurable variables##################################
## It is assumed admin, client and WORK are under this directory
## Default suggestions are for Stanford
APP_DIR = '<afs_path_to_home_dir>/cgi-bin/stat390' ## Change if you copy
APP_WEBROOT = '<your_web_URL>/cgi-bin/stat390' ## Note URL!
APP_LOGGING = False  ## Allowable values True/False
LOG_DIR = APP_DIR + '/LOG' ## If logging is true above, ensure this exists
SMTP_SERVER = 'smtp.yourdomain' ## e.g. smtp.stanford.edu
CONSULTANTS_CSV = APP_DIR + "/WORK/consultants/enrolled.csv" # change appropriately
INSTRUCTOR_EMAIL = "<sunet_id>@stanford.edu" # change appropriately

## display value; the corresponding blackout_time is computed below automatically
## i.e. AVAILABLE_DATES[i] will not be shown as a choice after BLACKOUT_TIMES[i]
## CHANGE THIS FOR EACH QUARTER
## Note: code to find blackout time is not great, don't push it. Or improve it. 
## ONLY allowed formats (spaces, commas important): 
##  "Jan 10, 10-12 noon" or "Feb 2, 12-2 pm" or "March 2, 9-11 am"
##
AVAILABLE_DATES = [ "Apr 1, 3-4 pm",
                    "Apr 13, 2-4 pm",
                    "Apr 13, 6-7 pm",
                    "Apr 15, 11-1 pm"]
## Advanced configuration possible in stat390common.py

