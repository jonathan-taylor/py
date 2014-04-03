#!/usr/bin/env python

import sys
sys.path.append("../WORK")

from stat390common import *

# create tables
Base.metadata.create_all(engine)

# Now create all consultants from csv file
import csv
reader = csv.DictReader(open(CONSULTANTS_CSV, "rU"), dialect="excel")
consultants = [Consultant(row['Email'], row['Name']) for row in reader]

# create a Session
session = sessionmaker(bind=engine)()
session.add_all(consultants)
session.commit()
session.close()
