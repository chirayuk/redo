import sys, os
import vars

# By default, no output colouring.
RED     = ""
GREEN   = ""
YELLOW  = ""
BLUE    = ""
MAGENTA = ""
CYAN    = ""
BLUE    = ""
BOLD    = ""
PLAIN   = ""

if sys.stderr.isatty() and (os.environ.get('TERM') or 'dumb') != 'dumb':
    # ...use ANSI formatting codes.
    RED     = "\x1b[31m"
    GREEN   = "\x1b[32m"
    YELLOW  = "\x1b[33m"
    BLUE    = "\x1b[34m"
    MAGENTA = "\x1b[35m"
    CYAN    = "\x1b[36m"
    BOLD    = "\x1b[1m"
    PLAIN   = "\x1b[m"

LOG_COLOR  = BLUE
WARN_COLOR = MAGENTA
ERR_COLOR  = RED

def log_(s):
    sys.stdout.flush()
    if vars.DEBUG_PIDS:
        sys.stderr.write('%d %s' % (os.getpid(), s))
    else:
        sys.stderr.write(s)
    sys.stderr.flush()


def log(s):
    log_(''.join([LOG_COLOR,  BOLD, "redo  ", PLAIN, LOG_COLOR, vars.DEPTH, s]))

def err(s):
    log_(''.join([ERR_COLOR,  BOLD, "redo  ", PLAIN, ERR_COLOR, vars.DEPTH, s]))

def warn(s):
    log_(''.join([WARN_COLOR, BOLD, "redo  ", PLAIN, WARN_COLOR, vars.DEPTH, s]))


def debug(s):
    if vars.DEBUG >= 1:
        log_('redo: %s%s' % (vars.DEPTH, s))
def debug2(s):
    if vars.DEBUG >= 2:
        log_('redo: %s%s' % (vars.DEPTH, s))
def debug3(s):
    if vars.DEBUG >= 3:
        log_('redo: %s%s' % (vars.DEPTH, s))


