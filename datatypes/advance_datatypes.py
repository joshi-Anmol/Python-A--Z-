import arrow

time_used = arrow.utcnow()
time_used.to("Europe/Rome")

from collections import namedtuple
time_profile = namedtuple("time_profile", ["value1" ,"value2"])


