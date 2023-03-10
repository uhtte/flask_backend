# -*- coding:utf-8 -*-
import os
import traceback

__author__ = "yongil80.cho@samsung.com"
__copyright__ = "Copyright 2022, Samsung Electronics"


def get_callstack():
    lines = traceback.format_exc().strip().split("\n")
    rl = [lines[-1]]
    lines = lines[1:-1]
    lines.reverse()
    nstr = ""
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith('File "'):
            eles = lines[i].strip().split('"')
            basename = os.path.basename(eles[1])
            lastdir = os.path.basename(os.path.dirname(eles[1]))
            eles[1] = "%s/%s" % (lastdir, basename)
            rl.append("^\t%s %s" % (nstr, '"'.join(eles)))
            nstr = ""
        else:
            nstr += line

    return "\n".join(rl)
